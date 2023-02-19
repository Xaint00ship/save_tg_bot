import telebot
import db
from datetime import datetime


token = open('TgToken.txt', 'r').read()
bot = telebot.TeleBot(token)


# Отслеживаем добавление в чат, при добавлении в чат, создается таблица.
@bot.message_handler(content_types=['new_chat_members'])
def add_new_chat(message, res=False):
    db.create_table(message.chat.title)

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document',
    'text', 'location', 'contact', 'sticker'])

def handle_text(message):


    # Формируем данные для занесения в таблицу из сообщения.

    data = {
        "timestamp": datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S'), # Форматируем дату из UNIX
        "message_id": message.message_id,
        "telegram_user_id": message.from_user.id,
        "type": message.content_type,
        "text": message.text,
        "reply_to": 0,
        "table_name": message.chat.title
    }

    # Проверка на реплай
    try:
        data["reply_to"] = message.reply_to_message.message_id
    except:
        pass

    # Проверка на наличии caption
    if message.content_type != "text" and message.caption != None:
        data["text"] = message.caption
    elif message.content_type != "text":
        data["text"] = ""

    # Добавление записи в таблицу.
    db.add_msg(data)






bot.polling(none_stop=True, interval=0)

