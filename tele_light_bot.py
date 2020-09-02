!pip install adafruit-io
!pip install python-telegram-bot 
import os 
from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
import requests 
x = os.getenv('ADAFRUIT_IO_USERNAME')
y = os.getenv('ADAFRUIT_IO_KEY')

from Adafruit_IO import Client, Feed
aio = Client(x,y) 

def start(bot,update):
    bot.send_message(chat_id = update.effective_chat.id,text="Hi Welcome to Vilton's First Bot! You know, its going to be amazing. Lets Chat")
    

def light_on(bot,update):
    from Adafruit_IO import Data
    # Sending a value to a feed
    value = Data(value=1)
    value_send = aio.create_data('vbot',value)
    bot.send_message(chat_id = update.effective_chat.id,text="Turning Light On")
    bot.sendPhoto(chat_id=update.effective_chat.id, photo='https://images.squarespace-cdn.com/content/5784e04246c3c41c72bf6305/1468526448115-KB10QTHCWSJ3IHHK7HVP/640px-Bombeta_de_Llum.jpg?content-type=image%2Fjpeg')

def light_off(bot,update):
    from Adafruit_IO import Data
    # Sending a value to a feed
    value = Data(value=0)
    value_send = aio.create_data('vbot',value)
    bot.send_message(chat_id = update.effective_chat.id,text="Turning Light Off")
    bot.sendPhoto(chat_id=update.effective_chat.id, photo='https://ak.picdn.net/shutterstock/videos/16051507/thumb/1.jpg')

a = Updater('1212708416:AAE4KlunY3DDDJVhIvLKo8kxx0h4pA_R0mE')
dp = a.dispatcher 
dp.add_handler(CommandHandler('lighton',light_on)) 
dp.add_handler(CommandHandler('lightoff',light_off))
dp.add_handler(CommandHandler('start', start))
a.start_polling()
a.idle() 
