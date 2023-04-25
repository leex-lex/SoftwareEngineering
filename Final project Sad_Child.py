import telebot
import psutil
import os

readpath ='tokenn.txt'
tocken=''

with open(readpath) as f:
    tocken = f.read()
    print (tocken)
bot = telebot.TeleBot(tocken)

with open("games.txt") as games_list:
    GAMES = games_list.readlines()

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text=="/start":
        markup = telebot.types.ReplyKeyboardMarkup()
        item=telebot.types.KeyboardButton("Проверить")
        markup.add(item)
        bot.send_message(message.chat.id,"Этот бот позволит вам контролировать, чем занимается ребенок за компьютером. Используйте кнопки для взаимодействия", reply_markup=markup)
    if message.text == "Проверить":
        markup = telebot.types.ReplyKeyboardMarkup()
        games = check_games()
        if len(games) > 0:
            item1=telebot.types.KeyboardButton("Проверить")
            item2=telebot.types.KeyboardButton("Выключить компьютер")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.from_user.id,
                             f'На компьютере ребенка запущены следующие игры: {"".join(games)}', reply_markup=markup)
        else:
            item=telebot.types.KeyboardButton("Проверить")
            markup.add(item)
            bot.send_message(message.from_user.id,
                             f'Не найдено запущенных игр', reply_markup=markup)
    if message.text == "Выключить компьютер":
        markup = telebot.types.ReplyKeyboardMarkup()
        item=telebot.types.KeyboardButton("Проверить")
        markup.add(item)
        off()
        bot.send_message(message.from_user.id,
                             f'Компьютер ребенка будет выключен через 10 минут', reply_markup=markup)

def check_games():
    out=[]
    for i in psutil.pids():
        try:
            p = psutil.Process(i)
        except psutil.NoSuchProcess:
            continue
        if p.name() in GAMES:
            out.append(p.name())
    return out

def off():
    os.system("shutdown -s -t 600")        
bot.polling(none_stop=True, interval=0)
