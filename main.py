import telebot
import requests
from dotenv import load_dotenv
import os
load_dotenv()
from request_edit import NewsRequest
TG_KEY= str(os.getenv("TELEGRAM_KEY"))
API_NEWS_KEY = str(os.getenv("API_KEY"))

bot = telebot.TeleBot(TG_KEY)
n = NewsRequest()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Бот отправляет сегодняшние новости по команде /tnews')

@bot.message_handler(commands=['tnews'])
def take_news(message):
    data = n.take_actual_news()
    for i in range(len(data)//3):
        bot.send_message(message.chat.id, i )


bot.polling(non_stop=True)