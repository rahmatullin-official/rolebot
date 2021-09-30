import telebot
from telebot import types
import sqlite3
from config import my_token

mybot = telebot.TeleBot(my_token)


@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id,
                       "Здравсвуйте {0.first_name}! Здесь будут появлятся новости и сообщения!".format(message.from_user))
    new_user_add(message)


def new_user_add(message):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
          id INTEGER, teacher INTEGER, teacher_class INTEGER, mkinfmat INTEGER, mkn INTEGER, mkiy INTEGER, mkfil INTEGER,
          mken INTEGER, mkfot INTEGER, mki INTEGER, adm INTEGER, nick TEXT NOT NULL );
       """)
    db.commit()

    people_id = message.chat.id
    n = f"@{message.from_user.username}"
    sql.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = sql.fetchone()
    if data:
        pass
    else:
        sql.execute(
            f"INSERT INTO users(id, teacher, teacher_class, mkinfmat, mkn, mkiy, mkfil, mken, mkfot, mki, adm, nick) VALUES ({people_id}, 0,0,0,0,0,0,0,0,0,0,'');")
        db.commit()
    sql.execute(f"UPDATE users SET nick=? WHERE id={message.chat.id};", [n])
    db.commit()


mybot.polling(none_stop=True)
