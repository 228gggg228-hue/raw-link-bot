import os
import telebot

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def fix(u):
    # GitHub raw
    if "raw.githubusercontent.com" in u:
        p = u.split("/")
        return "https://github.com/" + p[3] + "/" + p[4] + "/blob/" + p[5] + "/" + "/".join(p[6:])
    
    # GitHub Gist raw
    if "gist.githubusercontent.com" in u:
        return u.replace("gist.githubusercontent.com", "gist.github.com").replace("/raw/", "/")
    
    # GitLab raw
    if "gitlab.com" in u and "/-/raw/" in u:
        return u.replace("/-/raw/", "/-/blob/")
    
    # Bitbucket raw
    if "bitbucket.org" in u and "/raw/" in u:
        return u.replace("/raw/", "/src/")
    
    # Pastebin raw
    if "pastebin.com/raw/" in u:
        return u.replace("/raw/", "/")
    
    # Pastefy raw
    if "pastefy.app" in u and "/raw" in u:
        return u.replace("/raw", "")
    
    # Hastebin raw
    if "hastebin.com/raw/" in u:
        return u.replace("/raw/", "/")
    
    # dpaste raw
    if "dpaste." in u and "/raw/" in u:
        return u.replace("/raw/", "/")
    
    # ControlC raw
    if "controlc.com" in u and "/raw/" in u:
        return u.replace("/raw/", "/")
    
    return "Не знаю такую ссылку"

@bot.message_handler(func=lambda m: True)
def h(m):
    bot.reply_to(m, fix(m.text.strip()))

print("Бот запущен")
bot.polling(none_stop=True)
