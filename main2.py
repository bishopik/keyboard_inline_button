import telebot
from telebot import types

bot = telebot.TeleBot('1834841635:AAFVYR_uyCTmqkVjoFFRQwsTBcafT4zMiPY')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Кнопка 1")
    btn2 = types.KeyboardButton("👋 Кнопка 2")
    btn3 = types.KeyboardButton("❓ Задати питання")
    btn4 = types.KeyboardButton("/start")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот!".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.greet_kb)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Кнопка 1"):
        #bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Ссилка 1', url='https://aparat.ua')
        markup.add(btn_my_site)
        btn_my_site2 = types.InlineKeyboardButton(text='Ссилка 2', url='https://aparat.ua')
        markup.add(btn_my_site2)
        bot.send_message(message.chat.id, "Нажми на кнопку та перейди на наш сайт.", reply_markup=markup)

    elif (message.text == "👋 Кнопка 2"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Ссилка 1-1', url='https://aparat.ua')
        markup.add(btn_my_site)
        btn_my_site2 = types.InlineKeyboardButton(text='Ссилка 2-1', url='https://aparat.ua')
        markup.add(btn_my_site2)
        bot.send_message(message.chat.id, "Нажми на кнопку та перейди на наш сайт.", reply_markup=markup)

    elif (message.text == "❓ Задати питання"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Кнопка 2-1")
        btn2 = types.KeyboardButton("👋 Кнопка 2-2")
        btn4 = types.KeyboardButton("/start")
        back = types.KeyboardButton("Повернутись у головне меню")
        markup.add(btn1, btn2, back, btn4)
        bot.send_message(message.chat.id, text="Задайте мені питання", reply_markup=markup)

    elif (message.text == "👋 Кнопка 2-1"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site1 = types.InlineKeyboardButton(text='👋 Кнопка 2-1', url='https://aparat.ua')
        markup.add(btn_my_site1)
        bot.send_message(message.chat.id, "Нажми на кнопку та перейди на наш сайт.", reply_markup=markup)

    elif message.text == "👋 Кнопка 2-2":
        markup = types.InlineKeyboardMarkup()
        btn_my_site2 = types.InlineKeyboardButton(text='👋 Кнопка 2-2', url='https://aparat.ua')
        markup.add(btn_my_site2)
        bot.send_message(message.chat.id, "Нажми на кнопку та перейди на наш сайт.", reply_markup=markup)

    elif (message.text == "Повернутись у головне меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Кнопка 1")
        button2 = types.KeyboardButton("👋 Кнопка 2")
        button3 = types.KeyboardButton("❓ Задати питання")
        button4 = types.KeyboardButton("/start")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, text="Ви вернулись у головне меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На таку комманду я не запрограммован..")


bot.polling(none_stop=True)