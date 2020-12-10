from bot import hideToken

import telebot
bot = telebot.TeleBot(hideToken())

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'test')

bot.polling(none_stop=True, interval=0)