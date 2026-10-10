import os
import telebot

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def fix(u):
    if "raw.githubusercontent.com" in u:
        p = u.split("/")
        return "https://github.com/" + p[3] + "/" + p[4] + "/blob/" + p[5] + "/" + "/".join(p[6:])
    if "pastebin.com/raw/" in u:
        return u.replace("/raw/", "/")
    return "Не знаю такую ссылку"

@bot.message_handler(func=lambda m: True)
def h(m):
    bot.reply_to(m, fix(m.text.strip()))

print("Бот запущен")
bot.polling(none_stop=True)
