import telebot

BOT_TOKEN = ('5773482626:AAGfWoGsyqVvqM1ky-HLaYXod6v2pSvBgfA')
bot = telebot.TeleBot(BOT_TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Информатика', 'Математика', 'Русский язык', 'Английский')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет,какие задачи вас интересуют?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Информатика':
        bot.send_message(message.from_user.id, 'ссылка')

    elif message.text.lower() == 'Математика':
        bot.send_message(message.from_user.id, 'Numble: https://numble.wtf/')
        bot.send_message(message.from_user.id, 'Cogit: https://cogit.fun/play')
        bot.send_message(message.from_user.id, 'Angle: https://angle.wtf/', reply_markup=keyboard1)

    elif message.text.lower() == 'Русский язык':
        bot.send_message(message.from_user.id, 'wordle: https://wordle.belousov.one/', reply_markup=keyboard1)

    elif message.text.lower() == 'Английский':
        bot.send_message(message.from_user.id, 'squardle: https://fubargames.se/squardle/')
        bot.send_message(message.from_user.id, 'CONTEXTO: https://contexto.me/', reply_markup=keyboard1)

    elif message.text.lower() == 'География':
        bot.send_message(message.from_user.id, 'globle: https://globle-game.com/')
        bot.send_message(message.from_user.id, 'WORLDLE: https://worldle.teuteuf.fr/')
        bot.send_message(message.from_user.id, 'WORLDLE: https://worldle.teuteuf.fr/', reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)