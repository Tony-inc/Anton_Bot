import telebot
from telebot import types
from random import choice

bot = telebot.TeleBot('5374635129:AAG9l18dW7vpsHpIV4V13lW51nBVaIu_JVI')
kisses = ['https://media.giphy.com/media/lTQF0ODLLjhza/giphy.gif', 'https://media.giphy.com/media/dMYVHzANYb9p6/giphy.gif', 'https://media.giphy.com/media/Vi0Ws3t4JSLOgdkaBq/giphy-downsized-large.gif']
hugs = ['https://media.giphy.com/media/l8ooOxhcItowwLPuZn/giphy.gif', 'https://media.giphy.com/media/EvYHHSntaIl5m/giphy.gif', 'https://media.giphy.com/media/QbkL9WuorOlgI/giphy.gif']
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
    markup.add(kiss, hug, saying)
    bot.send_message(message.chat.id, 'Choose the option', reply_markup=markup)


@bot.message_handler(commands=['kiss'])
def help(message):
    bot.send_animation(message.chat.id, choice(kisses))

@bot.message_handler(commands=['hug'])
def help(message):
    bot.send_animation(message.chat.id, choice(hugs))

@bot.message_handler(commands=['saying'])
def help(message):
    bot.send_message(message.chat.id, choice(sayings))

@bot.message_handler()
def help(message):
    bot.send_message(message.chat.id, "I don't get it")


bot.polling(non_stop=True)