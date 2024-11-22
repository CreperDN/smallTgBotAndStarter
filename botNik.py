import telebot
from telebot import types
import requests
import threading
import schedule
import time
import os

TOKEN = "62???????:AA?????????????????????-EA"
bot = telebot.TeleBot(TOKEN)
def my_code():
    bothelper = telebot.TeleBot(TOKEN)
    chat_id = "20????????"
    

    print("started")

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        print("Someone started a chat on", time.localtime())
        bot.reply_to(message,
'''Some Text
More text'''.format(message.from_user), parse_mode='html',reply_markup=markup)


    @bot.message_handler(func=lambda message: True)
    def menu(message):
    	if message.chat.type == 'private':
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message.text}'
            print(requests.get(url).json())
            bot.reply_to(message, "Ваш відгук відправлено, дякуємо!".format(message.from_user), parse_mode='html')


    bot.polling()

def stop_code():
    print("stopped")
    bot.stop_polling()
    os._exit(69)

def run_thread():
    threading.Thread(target=my_code).start()

schedule.every().day.at("00:19").do(stop_code)

run_thread()

while True:
    schedule.run_pending()
    time.sleep(1)