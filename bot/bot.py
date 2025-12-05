import config
from telebot import TeleBot

bot = TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,"Бот работает! Привет")

@bot.message_handler(commands=["help"])
def start(message):
    bot.reply_to(message,"""
/start - Запуск бота
/help - Показывает все команды бота
""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Данной команды не существует")
    


bot.infinity_polling()