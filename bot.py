import os
import telebot
import requests
from telebot import types

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
PASTEFY_TOKEN = os.environ.get("PASTEFY_TOKEN")
bot = telebot.TeleBot(TOKEN)

links = {}

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
    except Exception as e:
        return None

def upload_to_pastefy(text):
    """Загружает текст в Pastefy, возвращает ссылку или None"""
    try:
        r = requests.post(
            "https://pastefy.app/api/v2/paste",
            headers={"Authorization": "Bearer " + PASTEFY_TOKEN},
            json={"content": text, "title": "from bot"},
            timeout=20
        )
        data = r.json()
        paste_id = data.get("paste", {}).get("id")
        if paste_id:
            return "https://pastefy.app/" + paste_id
    except Exception:
        pass
    return None

@bot.message_handler(func=lambda m: "http" in m.text)
def handle_link(m):
    u = m.text.strip()
    links[m.chat.id] = u
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📎 В raw", callback_data="to_raw"),
        types.InlineKeyboardButton("✂️ Без raw", callback_data="from_raw"),
        types.InlineKeyboardButton("📄 Отправить файлом", callback_data="send_file"),
        types.InlineKeyboardButton("📦 В Pastefy", callback_data="to_pastefy"),
        types.InlineKeyboardButton("🎮 В loadstring", callback_data="to_loadstring"),
    )
    bot.reply_to(m, "Что сделать со ссылкой?", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: True)
def handle_button(c):
    u = links.get(c.message.chat.id, "")
    if not u:
        bot.answer_callback_query(c.id, "Ссылка потерялась, отправь заново")
        return

    if c.data == "to_raw":
        bot.send_message(c.message.chat.id, to_raw(u))
    elif c.data == "from_raw":
        bot.send_message(c.message.chat.id, from_raw(u))
    elif c.data == "send_file":
        text = fetch_text(u)
        if text is None:
            bot.send_message(c.message.chat.id, "Не удалось скачать содержимое")
        else:
            with open("/tmp/file.txt", "w", encoding="utf-8") as f:
                f.write(text)
            with open("/tmp/file.txt", "rb") as f:
                bot.send_document(c.message.chat.id, f)
    elif c.data == "to_pastefy":
        text = fetch_text(u)
        if text is None:
            bot.send_message(c.message.chat.id, "Не удалось скачать содержимое")
        else:
            link = upload_to_pastefy(text)
            if link:
                bot.send_message(c.message.chat.id, "Готово: " + link)
            else:
                bot.send_message(c.message.chat.id, "Ошибка загрузки в Pastefy")
    elif c.data == "to_loadstring":
        bot.send_message(c.message.chat.id, 'loadstring(game:HttpGet("' + u + '"))()')

    bot.answer_callback_query(c.id)

print("Бот запущен")
bot.polling(none_stop=True)
