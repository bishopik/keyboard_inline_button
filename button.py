import telebot
from telebot import types

# токен моего бота
bot = telebot.TeleBot(' "ВВЕДІТЬ  ВАШ  ТОКЕН ')

# при старте меню
@bot.message_handler(commands=["start"])
def markup(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    Catalog = types.KeyboardButton(text="Каталог")
    Info = types.KeyboardButton(text="Інформація")
    markup.add(Catalog, Info)
    bot.send_message(message.chat.id, "Ласкаво просимо до магазину цифрових товарів", reply_markup=markup)

# условие при вибору Каталог
@bot.message_handler(content_types=['text'])
def catalogKBoard(message):
    if message.text == "Каталог":
        catalogKBoard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        Steam = types.KeyboardButton(text="Кнопка 1")
        Origin = types.KeyboardButton(text="Кнопка 2")
        UPlay = types.KeyboardButton(text="Кнопка 3")
        back = types.KeyboardButton("Повернутись у головне меню")
        catalogKBoard.add(Steam, Origin, UPlay, back)
        bot.send_message(message.chat.id, "Вибиріть категорію", reply_markup=catalogKBoard)

# умова вибору кнопки Інформація
    elif (message.text == "Інформація"):
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, "Тут ваша інформація вся", reply_markup=markup)

# умова вибору кнопки Steam
    elif (message.text == "Кнопка 1"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Силка Кнопка 2', url='https://aparat.ua')
        markup.add(btn_my_site)
        btn_my_site2 = types.InlineKeyboardButton(text='Силка Кнопка 2', url='https://aparat.ua')
        markup.add(btn_my_site2)
        bot.send_message(message.chat.id, "Натистни на кнопку та перейди на наш сайт.", reply_markup=markup)

# умова вибору кнопки UPlay без ссилок
    elif (message.text == "Кнопка 2"):
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, "Ви отримали простий текст без силки", reply_markup=markup)

# умова вибору кнопки Origin
    elif (message.text == "Кнопка 3"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Силка Кнопка 3', url='https://aparat.ua')
        markup.add(btn_my_site)
        btn_my_site2 = types.InlineKeyboardButton(text='Силка Кнопка 3', url='https://aparat.ua')
        markup.add(btn_my_site2)
        bot.send_message(message.chat.id, "Натисни на кнопку та перейди на наш сайт.", reply_markup=markup)

# умова вибору кнопки Повернутись у головне меню
    elif (message.text == "Повернутись у головне меню"):
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        Catalog = types.KeyboardButton(text="Каталог")
        Info = types.KeyboardButton(text="Інформація")
        markup.add(Catalog, Info)
        bot.send_message(message.chat.id, "Ви вернулись у головне меню", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="На таку комманду я не запрограммован..")


bot.polling(none_stop=True)