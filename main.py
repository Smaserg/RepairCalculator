import telebot
from telebot import types

bot = telebot.TeleBot('1931611460:AAEruzNTT6e_bqHTPu3lQXa5V7pf7AWBIrc')

name = ''
surname = ''


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши Привет')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.chat.id, 'Поздравляю, Вы решили сделать ремонт?')
    bot.register_next_step_handler(message, flat_area)


def flat_area(message):
    global first_area
    first_area = message.text
    bot.send_message(message.chat.id, 'Сколько квадратных метров по стенам в первой комнате?')
    bot.register_next_step_handler(message, member)


def member(message):
    global member1
    member1 = message.text
    bot.send_message(message.chat.id, 'Запомнил')

    keyboard = types.InlineKeyboardMarkup()
    key_painting = types.InlineKeyboardButton(text='Покраска', callback_data='painting')
    keyboard.add(key_painting)
    key_decor = types.InlineKeyboardButton(text='Декоративная штукатурка', callback_data='decor')
    keyboard.add(key_decor)
    question = 'Вы, ' + name + ' ' + surname + ', хотите покрасить комнату или нанести декоративную штукатурку?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    bot.register_next_step_handler(message, second_flat_area)


def second_flat_area(message):
    global second_area
    global member1
    bot.register_next_step_handler(message, member1)
    member1 = message.text
    bot.send_message(message.chat.id, 'Запомнил')
    keyboard = types.InlineKeyboardMarkup()
    key_painting = types.InlineKeyboardButton(text='Покраска', callback_data='painting')
    keyboard.add(key_painting)
    key_decor = types.InlineKeyboardButton(text='Декоративная штукатурка', callback_data='decor')
    keyboard.add(key_decor)
    question = 'Вы, ' + name + ' ' + surname + ', хотите покрасить комнату или нанести декоративную штукатурку?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    bot.register_next_step_handler(message, third_flat_area)


def third_flat_area(message):
    global third_area
    global member1
    bot.register_next_step_handler(message, member1)
    member1 = message.text
    bot.send_message(message.chat.id, 'Запомнил')
    keyboard = types.InlineKeyboardMarkup()
    key_painting = types.InlineKeyboardButton(text='Покраска', callback_data='painting')
    keyboard.add(key_painting)
    key_decor = types.InlineKeyboardButton(text='Декоративная штукатурка', callback_data='decor')
    keyboard.add(key_decor)
    question = 'Вы, ' + name + ' ' + surname + ', хотите покрасить комнату или нанести декоративную штукатурку?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    bot.register_next_step_handler(message, full_price)


def full_price(message):
    global listallarea
    global listarea
    listarea = []
    listarea.append(pricepainting)
    listarea.append(pricedecor)
    listallarea = sum(listarea)
    bot.send_message(message.from_user.id, ' Cтоимость всего ремонта составит ' + str(listallarea) + ' долларов')

    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://krasdom.by/index.php')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id,"На сайте Красочного дома, Вы, можете ознакомиться с материалами и галереей работ наших мастеров",reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global pricepainting
    global pricedecor
    if call.data == 'painting':
        pricepainting = (int(member1) * 8)
        bot.send_message(call.message.chat.id, 'Комнату будем красить. ''Стоимость ремонта: ' + str(
            pricepainting) + ' долларов. ' 'Сколько квадратных метров следующая комната?')
    elif call.data == 'decor':
        pricedecor = (int(member1) * 17)
        bot.send_message(call.message.chat.id,
                         'В комнате будем наносить декоративную штукатурку. ''Стоимость ремонта: ' + str(
                             pricedecor) + ' долларов. ' 'Сколько квадратных метров следующая комната?')

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception:
      pass