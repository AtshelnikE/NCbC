import telebot, os
from neuronet import predict

TOKEN = '6705723984:AAFAgh83wrzisLftff7Pdw42PC74bfv42zQ'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который использует нейронную сеть")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # try:
    if len(message.text.split()) > 500:
        bot.send_message(message.chat.id,'Сообщение слишком длинное, невозможно идентифицировать')
    else:
        prediction = predict(message.text)
        bot.send_message(message.chat.id, prediction)
    # except Exception as e:
    #     bot.send_message(message.chat.id, "Произошла ошибка при предсказании. Пожалуйста, попробуйте еще раз.")
    #     print(e)

bot.polling(none_stop=True)