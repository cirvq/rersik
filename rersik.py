import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['hi'])
def welcome(message):
    bot.send_message(message.chat.id, "привет {0.first_name}, я рерсик".format(message.from_user, bot.get_me()))

@bot.message_handler(commands=['zalupa'])
def send(message):
    bot.send_message(message.chat.id, "😻".format(message.from_user, bot.get_me()))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'залупа':
        bot.reply_to(message, "🐈")
    if message.text.lower() == 'пиздюк молчит':
        bot.send_message(message.chat.id, 'абэ рерсика не лове')
    if message.text.lower() == 'абэ рерсика не лове':
        bot.send_message(message.chat.id, 'но я ему дала пиздюлейшинства')
    if message.text.lower() == 'но я ему дала пиздюлейшинства':
        bot.send_message(message.chat.id, 'и он записчал')
    if message.text.lower() == 'и он записчал':
        bot.send_message(message.chat.id, 'мой поцаненок то игривый')
    if message.text.lower() == 'мой поцаненок то игривый':
        bot.send_message(message.chat.id, 'но не какал он аналом')
    if message.text.lower() == 'но не какал он аналом':
        bot.send_message(message.chat.id, 'так то я люблю рерсик')
    if message.text.lower() == 'так то я люблю рерсик':
        bot.send_message(message.chat.id, 'а он нет')

bot.polling(none_stop=True)
