import  telebot
import  Config
from telebot import types
import requests
import bs4
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
         
cred = credentials.Certificate("Nerti.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://nerti-18551.firebaseio.com/'})


bot = telebot.TeleBot(Config.Token)



@bot.message_handler(commands=['start'])
def start (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['7 klass', '8 klass', '9 klass', '10 klass']])
    m = bot.send_message(message.chat.id, 'Выбери класс',  reply_markup=keyboard)
    bot.register_next_step_handler(m, answer)
    
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == '7 klass':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Плотность', 'Механическая работа', 'Масса', 'Гидравлический пресс', 'Давление в жидкостях', 'Давление твердых тел', 'Закон Архимеда', 'КПД', 'Кинетическая энергия', 'Механическая работа:', 'Мощность', 'Потенциальная энергия', 'Путь', 'Сила тяжести', 'Скорость', 'Назад' ]])
        m = bot.send_message(message.chat.id, 'Выбери тему',  reply_markup=keyboard)
        bot.register_next_step_handler(m, send)
    if message.text == '8 klass':
         keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
         keyboard.add(*[types.KeyboardButton(name) for name in ['Закон Архимеда', 'Закон Ома', 'Количество теплоты', 'Мощность тока', 'Напряжение', 'Напряжение1', 'Работа тока', 'Сила тока', 'Сила тока1', 'Сопротивление', 'Сопротивление проводника', 'Сопротивление1', 'Тепловое действие тока', 'Теплота парообразования', 'Теплота сгорания',  'Назад']])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
         m = bot.send_message(message.chat.id, 'Выбери тему',  reply_markup=keyboard)
         bot.register_next_step_handler(m, send1)
    if message.text == '9 klass':
         keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
         keyboard.add(*[types.KeyboardButton(name) for name in ['Гидравлический пресс', 'Давление в жидкостях', 'Давление твердых тел', 'Закон Архимеда', 'Закон сохранения импульса', 'Закон сохранения энергии', 'Импульс', 'Координата', 'Механическая работа', 'Момент силы', 'Путь Равноускоренное движение', 'Равнодействующая сила', 'Сила трения', 'Сила тяжести, вес', 'Сила упругости', 'Угловая скорость', 'Ускорение', 'Ускорение Криволинейное движение по окружности', 'Энергия пружины', 'Назад']])                                                                                                                                                                                                                                                                                                                                                                                                                
         m = bot.send_message(message.chat.id, 'Выбери тему',  reply_markup=keyboard)
         bot.register_next_step_handler(m, send2)
    if message.text == '10 klass':
         keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
         keyboard.add(*[types.KeyboardButton(name) for name in ['Внутренняя энергия газа', 'Давление идеального газа', 'Закон Кулона', 'Закон Менделеева-Клайперона', 'Закон всемирного тяготения', 'Заряд', 'Изобарический процесс', 'Изотермический процесс', 'Изохорический процесс', 'Напряженность поля', 'Первый закон термодинамики', 'Потенциал поля', 'ЭДС', 'Электроемкость', 'Энергия газа', 'Энергия конденсатора', 'Назад']])
         m = bot.send_message(message.chat.id, 'Выбери тему',  reply_markup=keyboard)
         bot.register_next_step_handler(m, send3)
    if message.text == 'Назад':
        start(message)
    else:
        send(message) or send1(message) or send2(message) or send3(message)
def send(message):
    text = message.text
    ref = db.reference('/7-klass').get()
    for k, v in ref.items():
        if text == k:
            bot.send_message(message.chat.id, v)
    #else:
      #  send(message)
        
def send1(message):
    text = message.text
    ref = db.reference('/8-klass').get()
    for k, v in ref.items():
        if text == k:
            bot.send_message(message.chat.id, v)

            
def send2(message):
    text = message.text
    ref = db.reference('/9-klass').get()
    for k, v in ref.items():
        if text == k:
            bot.send_message(message.chat.id, v)

            
def send3(message):
    text = message.text
    ref = db.reference('/10-klass').get()
    for k, v in ref.items():
        if text == k:
            bot.send_message(message.chat.id, v)





bot.polling(none_stop=True) 


