# Getting started

This API is tested with Python 2.6, Python 2.7, Python 3.4, Pypy and Pypy 3. Install the library:
# Meet the bot:
   YouTube: https://youtu.be/-FPjcd9bvWI
   
   Telegram: https://t.me/UnibaguePocketBot
   
   Github: https://github.com/SubZKiller/UnibaguePocketBot
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
$ pip install pyTelegramBotAPI
```

## Usage

Before you start writing your first bot it is important you get your token form the @Botfather in telegram for the bot to work.
once you have your token we proced to insert it.

```python
import telebot

bot = telebot.TeleBot("TOKEN")
```
Congratulations you have now created your bot now you just need to program its answers to do this you have to write what the bot must answer if given the correct command

```python
@bot.message_handler(func=lambda message: message.text == "User input")
def command_text_info(m):
    bot.send_message(m.chat.id, "message bot replies")
```
in case you would like to create keaboards for easier user interface you can.

First you must create the keay board

```python
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Profesores')
itembtn2 = types.KeyboardButton('Salones')
itembtn3 = types.KeyboardButton('Laboratorios')
itembtn4 = types.KeyboardButton('Información')
name of keyboard.add(itembtn1, itembtn2, itembtn3, itembtn4)
```
This is the result of what we created

![View-on-GitHub](https://raw.githubusercontent.com/SubZKiller/UnibaguePocketBot/master/images/teclado.jpg)



Now we need to call it, we can do this after every bot reply
```python
@bot.message_handler(func=lambda message: message.text == "User input")

def  command_text_opcioneselectivas(m):

bot.send_message(m.chat.id, "Message bot reply", reply_markup=name of keayboard)
```

Apart from the basic message replying this API is also capable of  sending images, audios, links, and more. 
For more information to all of these functions visit: https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md

#How to send pictures
```python
@bot.message_handler(func=lambda message: message.text == "Image")

def  command_text_imagesender1(m):
bot.send_photo(m.chat.id, open('/home/vdesktop/Botimages/1.jpg', 'rb'))
```
#How to send an ubication
```python
@bot.message_handler(func=lambda message: message.text == "Xmensaje")

def  command_text_xubicationesender1(m):
bot.send_location(m.chat.id, lon, lat)
```

![View-on-GitHub](https://raw.githubusercontent.com/SubZKiller/UnibaguePocketBot/master/images/imagen%20y%20ubicacion.jpg)


# Tutor
[Harold F Murcia](www.haroldmurcia.com)


***
Visit the YouTube channel to see the video of the project and future improvements of [here](https://www.youtube.com/watch?v=4jBrwAoXW3M&t=2s).
***

