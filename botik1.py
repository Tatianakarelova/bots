import telebot

bot = telebot.TeleBot('dQAvtr5217562986:AAG0gdEv5VKqwKsuWAXDDRg8jfs74')
@bot.message_handler(content_types=['voice'])
def start(message:telebot.types.Message):
    bot.send_message(message.chat.id,'У тебя красивый голос')
bot.polling(none_stop=True)






