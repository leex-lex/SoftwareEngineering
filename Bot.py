import os
import telebot
readpath ='tokenn.txt'
tocken=''
with open(readpath) as f:
    tocken = f.read()
    print (tocken)
bot = telebot.TeleBot(tocken)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()