
import telebot
from telebot import types

# Создаем бота
BOT_TOKEN = ('5773482626:AAGfWoGsyqVvqM1ky-HLaYXod6v2pSvBgfA')
bot = telebot.TeleBot(BOT_TOKEN)
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Информатика")
        item2=types.KeyboardButton("Математика")
        item3=types.KeyboardButton("Русский")
        item4=types.KeyboardButton("Английский")
        item4=types.KeyboardButton("География")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(m.chat.id, 'Привет, какие задачи вас интересуют?',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1
    if message.text.strip() == 'Информатика':
            answer = 'Numble: https://numble.wtf/'
    # Если юзер прислал 2
    elif message.text.strip() == 'Математика':
            answer = 'wordle: https://wordle.belousov.one/'
    # Если юзер прислал 3
    elif message.text.strip() == 'Русский':
            answer = 'squardle: https://fubargames.se/squardle/'
    # Если юзер прислал 4
    elif message.text.strip() == 'Английский':
            answer = 'globle: https://globle-game.com/'
    # Если юзер прислал 5
    elif message.text.strip() == 'География':
            answer = 'WORLDLE: https://worldle.teuteuf.fr/'
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
