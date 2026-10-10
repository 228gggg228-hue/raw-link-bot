import os
import telebot
import requests
from telebot import types

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Хранилище ссылок по id сообщения
links = {}

def to_raw(u):
    """Преобразует обычную ссылку в raw"""
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
    """Преобразует raw-ссылку в обычную"""
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
    """Скачивает текст по ссылке"""
    try:
        r = requests.get(u, timeout=15)
        r.raise_for_status()
        return r.text
    except Exception as e:
        return "Ошибка загрузки: " + str(e)

@bot.message_handler(func=lambda m: "http" in m.text)
def handle_link(m):
    u = m.text.strip()
    links[m.chat.id] = u
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📎 В raw", callback_data="to_raw"),
        types.InlineKeyboardButton("✂️ Без raw", callback_data="from_raw"),
        types.InlineKeyboardButton("📋 Скопировать текст", callback_data="copy_text"),
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
    elif c.data == "copy_text":
        text = fetch_text(u)
        if len(text) > 4000:
            text = text[:4000] + "\n...(обрезано)"
        bot.send_message(c.message.chat.id, "```\n" + text + "\n```", parse_mode="Markdown")
    elif c.data == "send_file":
        text = fetch_text(u)
        with open("/tmp/file.txt", "w", encoding="utf-8") as f:
            f.write(text)
        with open("/tmp/file.txt", "rb") as f:
            bot.send_document(c.message.chat.id, f)
    elif c.data == "to_pastefy":
        # Просто даём ссылку на просмотр
        bot.send_message(c.message.chat.id, u.replace("/raw", ""))
    elif c.data == "to_loadstring":
        bot.send_message(c.message.chat.id, 'loadstring(game:HttpGet("' + u + '"))()')

    bot.answer_callback_query(c.id)

print("Бот запущен")
bot.polling(none_stop=True)
