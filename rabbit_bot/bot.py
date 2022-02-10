import config
import telebot
import requests

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def find_song(message):
    url = f'http://localhost:9081/crawl.json?spider_name=google_spider&url=https://www.google.com/search?q={message.text}+"holychords"&callback=parse_page'
    response = requests.get(url)
    return

bot.infinity_polling()
