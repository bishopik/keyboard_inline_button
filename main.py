import telebot
from telebot import types

bot = telebot.TeleBot('1834841635:AAFVYR_uyCTmqkVjoFFRQwsTBcafT4zMiPY')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привітання")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привіт! Я твій бот-помічник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Привітання':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Кнопка №1')
        btn2 = types.KeyboardButton('Кнопка №2')
        btn3 = types.KeyboardButton('Кнопка №3')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте ваше питання', reply_markup=markup) #ответ бота


    elif message.text == 'Кнопка №1':
        bot.send_message(message.from_user.id, 'Текст повідомлення ' + '[ссылке](https://aparat.ua)', parse_mode='Markdown')

    elif message.text == 'Кнопка №2':
        bot.send_message(message.from_user.id, 'Текст повідомлення ' + '[ссылке](https://aparat.ua)', parse_mode='Markdown')

    elif message.text == 'Кнопка №3':
        bot.send_message(message.from_user.id, 'Текст повідомлення ' + '[ссылке](https://aparat.ua)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть