  -screen              select image from root window
  -seed value          seed a new sequence of pseudo-random numbers
  -set property value  set an image property
  -silent              operate silently, i.e. don't ring any bells 
  -snaps value         number of screen snapshots
  -support factor      resize support: > 1.0 is blurry, < 1.0 is sharp
  -synchronize         synchronize image to storage device
  -taint               declare the image as modified
  -transparent-color color
                       transparent color
  -treedepth value     color tree depth
  -verbose             print detailed information about the image
  -virtual-pixel method
                       Constant, Edge, Mirror, or Tile
  -window id           select window with this id or name
                       root selects whole screen

Image Operators:
  -annotate geometry text
                       annotate the image with text
  -colors value        preferred number of colors in the image
  -crop geometry       preferred size and location of the cropped image
  -encipher filename   convert plain pixels to cipher pixels
  -extent geometry     set the image size
  -geometry geometry   preferred size or location of the image
  -help                print program options
  -monochrome          transform image to black and white
  -negate              replace every pixel with its complementary color 
  -quantize colorspace reduce colors in this colorspace
  -resize geometry     resize the image
  -rotate degrees      apply Paeth rotation to the image
  -strip               strip image of all profiles and comments
  -thumbnail geometry  create a thumbnail of the image
  -transparent color   make this color transparent within the image
  -trim                trim image edges
  -type type           image type

Miscellaneous Options:
  -debug events        display copious debugging information
  -help                print program options
  -list type           print a list of supported option arguments
  -log format          format of debugging information
  -version             print version information

By default, 'file' is written in the MIFF image format.  To
specify a particular image format, precede the filename with an image
format name and a colon (i.e. ps:image) or specify the image type as
the filename suffix (i.e. image.ps).  Specify 'file' as '-' for
standard input or output.
import: delegate library support not built-in '' (X11) @ error/import.c/ImportImageCommand/1304.
TOKEN: command not found
bot: command not found
def: command not found
 : command not found
 : command not found
 : command not found
 : command not found
 : command not found
 : command not found
@bot.message_handler(8230414795:AAFui4pm5-RsQ_3XnF_bb6bH63-oxT00CEgTrue): command not found
def: command not found
 : command not found
print("Бот: command not found
bot.polling(none_stop=True): command not found
[Documents]$ ls
bot.py
[Documents]$ rm bot.py
[Documents]$ nano bot.py
nano: command not found
[Documents]$ python -c "code = '''import telebot

TOKEN = \"8230414795:AAFui4pm5-RsQ_3XnF-bb6bH63-oxT00CEg\"
bot = telebot.TeleBot(TOKEN)

def fix(u):
    if \"raw.githubusercontent.com\" in u:
        p = u.split(\"/\")
        return \"https://github.com/\" + p[3] + \"/\" + p[4] + \"/blob/\" + p[5] + \"/\" + \"/\".join(p[6:])
    if \"pastebin.com/raw/\" in u:
        return u.replace(\"/raw/\", \"/\")
    return \"Не знаю такую ссылку\"

@bot.message_handler(func=lambda m: True)
def h(m):
    bot.reply_to(m, fix(m.text.strip()))

print(\"Бот запущен\")
bot.polling(none_stop=True)
'''
open('bot.py','w').write(code)
print('OK, файл создан')
"
  File "<string>", line 1
    "code = '''import telebot
    ^
SyntaxError: unterminated string literal (detected at line 1)
TOKEN: command not found
bot: command not found
def: command not found
 : command not found
 : command not found
 : command not found
 : command not found
 : command not found
 : command not found
m:: command not found
def: command not found
 : command not found
print("Бот: command not found
bot.polling(none_stop=True): command not found
': command not found
open('bot.py','w').write(code): command not found
print('OK,: command not found
.: command not found
[Documents]$ printf 'import telebot\n' > bot.py
printf: command not found
[Documents]$ printf 'TOKEN = "8230414795:AAFui4pm5-RsQ_3XnF-bb6bH63-oxT00CEg"\n' >> bot.py
printf: command not found
[Documents]$ printf 'bot = telebot.TeleBot(TOKEN)\n' >> bot.py
printf: command not found
[Documents]$ echo 'import telebot' > bot.py
[Documents]$ echo 'TOKEN = "8230414795:AAFui4pm5-RsQ_3XnF-bb6bH63-oxT00CEg"' >> bot.py
[Documents]$ echo 'bot = telebot.TeleBot(TOKEN)' >> bot.py
[Documents]$ echo 'def fix(u):' >> bot.py
[Documents]$ echo '    if "raw.githubusercontent.com" in u:' >> bot.py
[Documents]$ echo '        p = u.split("/")' >> bot.py
[Documents]$ echo '        return "https://github.com/" + p[3] + "/" + p[4] + "/blob/" + p[5] + "/" + "/".join(p[6:])' >> bot.py
[Documents]$ echo '    if "pastebin.com/raw/" in u:' >> bot.py
[Documents]$ echo '        return u.replace("/raw/", "/")' >> bot.py
[Documents]$ echo '    return "Не знаю такую ссылку"' >> bot.py
[Documents]$ echo '@bot.message_handler(func=lambda m: True)' >> bot.py
[Documents]$ echo 'def h(m):' >> bot.py
[Documents]$ echo '    bot.reply_to(m, fix(m.text.strip()))' >> bot.py
[Documents]$ echo 'print("Бот запущен")' >> bot.py
[Documents]$ echo 'bot.polling(none_stop=True)' >> bot.py
[Documents]$ cat bot.py
import telebot
TOKEN = "8230414795:AAFui4pm5-RsQ_3XnF-bb6bH63-oxT00CEg"
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
[Documents]$ python bot.py
Бот запущен
Traceback (most recent call last):
  File "/private/var/mobile/Containers/Data/Application/755578CF-5C78-4B57-A7DC-B948C77B9ABF/Documents/bot.py", line 15, in <module>
    bot.polling(none_stop=True)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/var/mobile/Containers/Data/Application/755578CF-5C78-4B57-A7DC-B948C77B9ABF/Library/lib/python3.13/site-packages/telebot/__init__.py", line 1255, in polling
    logger.info('Starting your bot with username: [@%s]', self.user.username)
                                                          ^^^^^^^^^
  File "/var/mobile/Containers/Data/Application/755578CF-5C78-4B57-A7DC-B948C77B9ABF/Library/lib/python3.13/site-packages/telebot/__init__.py", line 314, in user
    self._user = self.get_me()
                 ~~~~~~~~~~~^^
  File "/var/mobile/Containers/Data/Application/755578CF-5C78-4B57-A7DC-B948C77B9ABF/Library/lib/python3.13/site-packages/telebot/__init__.py", line 1442, in get_me
    apihelper.get_me(self.token)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "/var/mobile/Containers/Data/Application/755578CF-5C78-4B57-A7DC-B948C77B9ABF/Library/lib/python3.13/site-packages/telebot/apihelper.py", line 218, in get_me
    return _make_request(token, method_url)
  File "/var/mobile/Containers/Data/Application/755578CF-5C78-4B57-A7DC-B948C77B9ABF/Library/lib/python3.13/site-packages/telebot/apihelper.py", line 182, in _make_request
    json_result = _check_result(method_name, result)
  File "/var/mobile/Containers/Data/Application/755578CF-5C78-4B57-A7DC-B948C77B9ABF/Library/lib/python3.13/site-packages/telebot/apihelper.py", line 211, in _check_result
    raise ApiTelegramException(method_name, result, result_json)
telebot.apihelper.ApiTelegramException: A request to the Telegram API was unsuccessful. Error code: 401. Description: Unauthorized
[Documents]$ grep TOKEN bot.py
TOKEN = "8230414795:AAFui4pm5-RsQ_3XnF-bb6bH63-oxT00CEg"
bot = telebot.TeleBot(TOKEN)
[Documents]$ python -c "s=open('bot.py').read(); i=s.find('TOKEN = '); j=s.find(chr(10), i); s=s[:i] + 'TOKEN = \"8230414795:AAFui4pm5-RsQ_3XnF_bb6bH63-oxT00CEg\"' + s[j:]; open('bot.py','w').write(s); print('OK')"
OK
[Documents]$ grep TOKEN bot.py
TOKEN = "8230414795:AAFui4pm5-RsQ_3XnF_bb6bH63-oxT00CEg"
bot = telebot.TeleBot(TOKEN)
[Documents]$ python bot.py
Бот запущен
echo 'pyTelegramBotAPI' > requirements.txt
[Documents]$ echo 'import os
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
                                        bot.polling(none_stop=True)' > bot_new.py
'import os
Version: ImageMagick 7.1.1-41 Q8 arm d7d490223:20241115 https://imagemagick.org
Copyright: (C) 1999 ImageMagick Studio LLC
License: https://imagemagick.org/script/license.php
Features: Cipher DPC 
Delegates (built-in): bzlib freetype heic jng jpeg png tiff xml
Compiler: clang (16.0.0)
Usage: import [options ...] [ file ]

Image Settings:
  -adjoin              join images into a single multi-image file
  -border              include window border in the output image
  -channel type        apply option to select image channels
  -colorspace type     alternate image colorspace
  -comment string      annotate image with comment
  -compress type       type of pixel compression when writing the image
  -define format:option
                       define one or more image format options
  -density geometry    horizontal and vertical density of the image
  -depth value         image depth
  -descend             obtain image by descending window hierarchy
  -display server      X server to contact
  -dispose method      layer disposal method
  -dither method       apply error diffusion to image
  -delay value         display the next image after pausing
  -encipher filename   convert plain pixels to cipher pixels
  -endian type         endianness (MSB or LSB) of the image
  -encoding type       text encoding type
  -filter type         use this filter when resizing an image
  -format "string"     output formatted image characteristics
  -frame               include window manager frame
  -gravity direction   which direction to gravitate towards
  -identify            identify the format and characteristics of the image
  -interlace type      None, Line, Plane, or Partition
  -interpolate method  pixel color interpolation method
  -label string        assign a label to an image
  -limit type value    Area, Disk, Map, or Memory resource limit
  -monitor             monitor progress
  -page geometry       size and location of an image canvas
  -pause seconds       seconds delay between snapshots
  -pointsize value     font point size
  -quality value       JPEG/MIFF/PNG compression level
  -quiet               suppress all warning messages
  -regard-warnings     pay attention to warning messages
  -repage geometry     size and location of an image canvas
  -respect-parentheses settings remain in effect until parenthesis boundary
  -sampling-factor geometry
                       horizontal and vertical sampling factor
  -scene value         image scene number
  -screen              select image from root window
  -seed value          seed a new sequence of pseudo-random numbers
  -set property value  set an image property
  -silent              operate silently, i.e. don't ring any bells 
  -snaps value         number of screen snapshots
  -support factor      resize support: > 1.0 is blurry, < 1.0 is sharp
  -synchronize         synchronize image to storage device
  -taint               declare the image as modified
  -transparent-color color
                       transparent color
  -treedepth value     color tree depth
  -verbose             print detailed information about the image
  -virtual-pixel method
                       Constant, Edge, Mirror, or Tile
  -window id           select window with this id or name
                       root selects whole screen

Image Operators:
  -annotate geometry text
                       annotate the image with text
  -colors value        preferred number of colors in the image
  -crop geometry       preferred size and location of the cropped image
  -encipher filename   convert plain pixels to cipher pixels
  -extent geometry     set the image size
  -geometry geometry   preferred size or location of the image
  -help                print program options
  -monochrome          transform image to black and white
  -negate              replace every pixel with its complementary color 
  -quantize colorspace reduce colors in this colorspace
  -resize geometry     resize the image
  -rotate degrees      apply Paeth rotation to the image
  -strip               strip image of all profiles and comments
  -thumbnail geometry  create a thumbnail of the image
  -transparent color   make this color transparent within the image
  -trim                trim image edges
  -type type           image type

Miscellaneous Options:
  -debug events        display copious debugging information
  -help                print program options
  -list type           print a list of supported option arguments
  -log format          format of debugging information
  -version             print version information

By default, 'file' is written in the MIFF image format.  To
specify a particular image format, precede the filename with an image
format name and a colon (i.e. ps:image) or specify the image type as
the filename suffix (i.e. image.ps).  Specify 'file' as '-' for
standard input or output.
import: delegate library support not built-in '' (X11) @ error/import.c/ImportImageCommand/1304.
TOKEN: command not found
bot: command not found
def: command not found
 : command not found
 : command not found
 : command not found
 : command not found
 : command not found
 : command not found
m:: command not found
def: command not found
 : command not found
print("Бот: command not found
bot.polling(none_stop=True)': command not found
[Documents]$ echo 'import os' > bot_new.py
[Documents]$ echo 'import telebot' >> bot_new.py
[Documents]$ echo 'TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")' >> bot_new.py
[Documents]$ echo 'bot = telebot.TeleBot(TOKEN)' >> bot_new.py
[Documents]$ echo 'def fix(u):' >> bot_new.py
[Documents]$ echo '    if "raw.githubusercontent.com" in u:' >> bot_new.py
[Documents]$ echo '        p = u.split("/")' >> bot_new.py
[Documents]$ echo '        return "https://github.com/" + p[3] + "/" + p[4] + "/blob/" + p[5] + "/" + "/".join(p[6:])' >> bot_new.py
[Documents]$ echo '    if "pastebin.com/raw/" in u:' >> bot_new.py
[Documents]$ echo '        return u.replace("/raw/", "/")' >> bot_new.py
[Documents]$ echo '    return "Не знаю такую ссылку"' >> bot_new.py
[Documents]$ echo '@bot.message_handler(func=lambda m: True)' >> bot_new.py
[Documents]$ echo 'def h(m):' >> bot_new.py
[Documents]$ echo '    bot.reply_to(m, fix(m.text.strip()))' >> bot_new.py
[Documents]$ echo 'print("Бот запущен")' >> bot_new.py
[Documents]$ echo 'bot.polling(none_stop=True)' >> bot_new.py
[Documents]$ cat bot_new.py
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
[Documents]$ cat bot_new.py
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
[Documents]$ 
