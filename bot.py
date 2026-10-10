import os
import telebot
import requests
from telebot import types

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
PASTEFY_TOKEN = os.environ.get("PASTEFY_TOKEN")
bot = telebot.TeleBot(TOKEN)

links = {}
files = {}
paste_links = {}

def text_stats(text):
    lines = text.count("\n") + 1
    return str(len(text)) + " символов, " + str(lines) + " строк"

def to_raw(u):
    if "github.com" in u and "/blob/" in u:
        return u.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    if "pastefy.app" in u and "/raw" not in u:
        return u.rstrip("/") + "/raw"
    if "pastebin.com" in u and "/raw/" not in u:
        p = u.rstrip("/").split("/")
        return "https://pastebin.com/raw/" + p[-1]
    if "gitlab.com" in u and "/-/blob/" in u:
        return u.replace("/-/blob/", "/-/raw/")
    return u

def from_raw(u):
    if "raw.githubusercontent.com" in u:
        p = u.split("/")
        return "https://github.com/" + p[3] + "/" + p[4] + "/blob/" + p[5] + "/" + "/".join(p[6:])
    if "pastefy.app" in u and "/raw" in u:
        return u.replace("/raw", "")
    if "pastebin.com/raw/" in u:
        return u.replace("/raw/", "/")
    if "gitlab.com" in u and "/-/raw/" in u:
        return u.replace("/-/raw/", "/-/blob/")
    if "hastebin.com/raw/" in u:
        return u.replace("/raw/", "/")
    return u

def fetch_text(u):
    try:
        r = requests.get(u, timeout=15)
        r.raise_for_status()
        return r.text
    except Exception:
        return None

def upload_to_pastefy(text):
    if len(text) > 500000:
        return "❌ Файл слишком большой для Pastefy (" + str(len(text)) + " символов). Лимит ~500 000."
    try:
        r = requests.post(
            "https://pastefy.app/api/v2/paste",
            # headers={"Authorization": "Bearer " + PASTEFY_TOKEN},
            json={"content": text, "title": "from bot", "visibility": "PUBLIC"},
            timeout=30
        )
        if r.status_code == 413:
            return "❌ Pastefy отклонил файл: слишком большой (413)."
        if r.status_code >= 400:
            return "Ошибка Pastefy: " + str(r.status_code) + " " + r.text[:200]
        data = r.json()
        paste_id = data.get("paste", {}).get("id")
        if paste_id:
            return "https://pastefy.app/" + paste_id
        return "Нет ID в ответе: " + str(data)
    except Exception as e:
        return "Ошибка: " + str(e)

# --- Обработка ссылок ---
@bot.message_handler(func=lambda m: m.text and "http" in m.text)
def handle_link(m):
    u = m.text.strip()
    links[m.chat.id] = u

    text = fetch_text(u)
    if text is not None:
        info = "Что сделать со ссылкой?\n📊 " + text_stats(text)
    else:
        info = "Что сделать со ссылкой?\n⚠️ Не удалось скачать содержимое"

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📎 В raw", callback_data="to_raw"),
        types.InlineKeyboardButton("✂️ Без raw", callback_data="from_raw"),
        types.InlineKeyboardButton("📄 Отправить файлом", callback_data="send_file"),
        types.InlineKeyboardButton("📦 В Pastefy", callback_data="to_pastefy"),
        types.InlineKeyboardButton("🎮 В loadstring", callback_data="to_loadstring"),
    )
    bot.reply_to(m, info, reply_markup=markup)

# --- Обработка файлов ---
@bot.message_handler(content_types=["document"])
def handle_document(m):
    try:
        file_info = bot.get_file(m.document.file_id)
        file_bytes = bot.download_file(file_info.file_path)
        try:
            text = file_bytes.decode("utf-8")
        except UnicodeDecodeError:
            text = file_bytes.decode("latin-1", errors="ignore")

        files[m.chat.id] = text

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📦 Сохранить в Pastefy", callback_data="file_to_pastefy"))
        bot.reply_to(
            m,
            "Файл получен: " + m.document.file_name + "\n📊 " + text_stats(text) + "\nСохранить содержимое в Pastefy?",
            reply_markup=markup
        )
    except Exception as e:
        bot.reply_to(m, "Не удалось обработать файл: " + str(e))

@bot.callback_query_handler(func=lambda c: True)
def handle_button(c):
    chat_id = c.message.chat.id

    # --- Сохранение файла в Pastefy ---
    if c.data == "file_to_pastefy":
        text = files.get(chat_id)
        if not text:
            bot.answer_callback_query(c.id, "Файл потерялся, отправь заново")
            return
        result = upload_to_pastefy(text)
        bot.send_message(chat_id, result)
        if result.startswith("https://pastefy.app/"):
            paste_links[chat_id] = result
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("📎 Сделать raw", callback_data="paste_to_raw"),
                types.InlineKeyboardButton("🎮 Сделать loadstring", callback_data="paste_to_loadstring"),
            )
            bot.send_message(chat_id, "Что сделать с этой ссылкой?", reply_markup=markup)
        bot.answer_callback_query(c.id)
        return

    # --- Кнопки для ссылки на Pastefy ---
    if c.data == "paste_to_raw":
        u = paste_links.get(chat_id, "")
        if not u:
            bot.answer_callback_query(c.id, "Ссылка потерялась")
            return
        bot.send_message(chat_id, u + "/raw")
        bot.answer_callback_query(c.id)
        return

    if c.data == "paste_to_loadstring":
        u = paste_links.get(chat_id, "")
        if not u:
            bot.answer_callback_query(c.id, "Ссылка потерялась")
            return
        bot.send_message(chat_id, 'loadstring(game:HttpGet("' + u + '/raw"))()')
        bot.answer_callback_query(c.id)
        return

    # --- Обработка ссылок ---
    u = links.get(chat_id, "")
    if not u:
        bot.answer_callback_query(c.id, "Ссылка потерялась, отправь заново")
        return

    if c.data == "to_raw":
        bot.send_message(chat_id, to_raw(u))
    elif c.data == "from_raw":
        bot.send_message(chat_id, from_raw(u))
    elif c.data == "send_file":
        text = fetch_text(u)
        if text is None:
            bot.send_message(chat_id, "Не удалось скачать содержимое")
        else:
            with open("/tmp/file.txt", "w", encoding="utf-8") as f:
                f.write(text)
            with open("/tmp/file.txt", "rb") as f:
                bot.send_document(chat_id, f)
    elif c.data == "to_pastefy":
        text = fetch_text(u)
        if text is None:
            bot.send_message(chat_id, "Не удалось скачать содержимое")
        else:
            result = upload_to_pastefy(text)
            bot.send_message(chat_id, result)
    elif c.data == "to_loadstring":
        raw_url = u
        if "pastefy.app" in raw_url and "/raw" not in raw_url:
            raw_url = raw_url.rstrip("/") + "/raw"
        elif "github.com" in raw_url and "/blob/" in raw_url:
            raw_url = raw_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
        elif "pastebin.com" in raw_url and "/raw/" not in raw_url:
            p = raw_url.rstrip("/").split("/")
            raw_url = "https://pastebin.com/raw/" + p[-1]
        elif "gitlab.com" in raw_url and "/-/blob/" in raw_url:
            raw_url = raw_url.replace("/-/blob/", "/-/raw/")
        bot.send_message(chat_id, 'loadstring(game:HttpGet("' + raw_url + '"))()')

    bot.answer_callback_query(c.id)

print("Бот запущен")
bot.polling(none_stop=True)
