import telebot
from telebot import types
from random import choice
from api import Giphy
import os
import pdftotext
import pyttsx3
from gtts import gTTS

extension = 'mp3'
voice = False
n = 1
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
    file = types.KeyboardButton('/resume')
    convert = types.KeyboardButton('/convert')
    markup.add(kiss, hug, saying, joke, iss_location, file, convert)
    bot.send_message(message.chat.id, 'Choose the option', reply_markup=markup)


@bot.message_handler(commands=['convert'])
def help_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pdf_to_mp3 = types.KeyboardButton('/pdf_to_mp3')
    pdf_to_wav = types.KeyboardButton('/pdf_to_wav')
    voice = types.KeyboardButton('/text_to_voice')
    help = types.KeyboardButton('/help')
    markup.add(pdf_to_mp3, pdf_to_wav, help, voice)
    bot.send_message(message.chat.id, 'Choose the option_2', reply_markup=markup)


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

@bot.message_handler(commands=['resume'])
def file(message):
    with open('test.pdf', 'rb') as f:
        # pdf = pdftotext.PDF(f)
        # file_to_send = f.read()
        bot.send_document(message.chat.id, f)


def convert_pdf(original_filepath: str, converted_filename: str, extension: str):
    with open(original_filepath, 'rb') as f:
        pdf = pdftotext.PDF(f)

    speak = pyttsx3.init()
    speak.save_to_file(pdf[0], f'{converted_filename}.{extension}')

    # speak.say(pdf[1])
    speak.runAndWait()

# content_types=['document', 'photo', 'audio', 'video', 'voice']

@bot.message_handler(content_types=['document'])
def pdf_to_audio(message):
    global extension
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    convert_pdf(file_name, f'converted-{file_name.split(".")[0]}', extension)

    with open(f'converted-{file_name.split(".")[0]}.{extension}', 'rb') as f:
        # pdf = pdftotext.PDF(f)
        # file_to_send = f.read()
        bot.send_document(message.chat.id, f)

    os.remove(file_name)
    os.remove(f'converted-{file_name.split(".")[0]}.{extension}')


@bot.message_handler(commands=['pdf_to_mp3'])
def pdf_to_mp3(message):
    bot.send_message(message.chat.id, 'Please send the file')
    global extension
    extension = 'mp3'


@bot.message_handler(commands=['pdf_to_wav'])
def pdf_to_wav(message):
    bot.send_message(message.chat.id, 'Please send the file')
    global extension
    extension = 'wav'

@bot.message_handler(commands=['text_to_voice'])
def voice(message):
    global n
    if n % 2 == 0:
        bot.send_message(message.chat.id, 'Please send the message')
        global voice
        voice = True
    else:
        bot.send_message(message.chat.id, 'The voice mode is off')
        voice = False
    n += 1



@bot.message_handler()
def message(message):
    if voice:

        file_name = 'name.mp3'
        text_to_mp3 = gTTS(message.text)
        text_to_mp3.save(file_name)

        audio = open(file_name, 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.id)
        os.remove(file_name)

    else:
        bot.send_message(message.chat.id, "I don't get it")





# convert_pdf('test.pdf', 'converted-test', 'mp3')





bot.polling(non_stop=True)