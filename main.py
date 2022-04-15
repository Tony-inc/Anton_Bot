import telebot
from telebot import types
from random import choice
from api import Giphy

giphy = Giphy()
bot = telebot.TeleBot('5374635129:AAG9l18dW7vpsHpIV4V13lW51nBVaIu_JVI')
sayings = ['I love you like a fat kid loves cake.', 'You want to know who I am in love with? Read the first word again.', 'I love you with all my belly. I would say heart, but my belly is bigger.']

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!\nI am a <em>lovely_anton_bot</em> :)\n<b>Anton</b> has created me to help him take care of you, when he is not nearby.\nI can hug 🤗 you, kiss 😘 you or just say something nice 🥰\nType /help to choose the option :)', parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kiss = types.KeyboardButton('/kiss')
    hug = types.KeyboardButton('/hug')
    saying = types.KeyboardButton('/saying')
    joke = types.KeyboardButton('/joke')
    iss_location = types.KeyboardButton('/iss')
    markup.add(kiss, hug, saying, joke, iss_location)
    bot.send_message(message.chat.id, 'Choose the option', reply_markup=markup)


@bot.message_handler(commands=['kiss'])
def kiss(message):
    bot.send_animation(message.chat.id, giphy.get_url("kiss"))

@bot.message_handler(commands=['hug'])
def hug(message):
    bot.send_animation(message.chat.id, giphy.get_url("hug"))

@bot.message_handler(commands=['saying'])
def saying(message):
    bot.send_message(message.chat.id, choice(sayings))

@bot.message_handler(commands=['joke'])
def joke(message):
    bot.send_message(message.chat.id, giphy.get_joke()[0])
    bot.send_message(message.chat.id, giphy.get_joke()[1])

@bot.message_handler(commands=['iss'])
def iss(message):
    bot.send_location(message.chat.id, giphy.location()[0], giphy.location()[1])

@bot.message_handler()
def message(message):
    bot.send_message(message.chat.id, "I don't get it")

bot.polling(non_stop=True)