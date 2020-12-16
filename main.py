import bot.config.config as TOKEN

import telebot

bot = telebot.TeleBot(TOKEN.token())