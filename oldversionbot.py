import telebot
from telebot import types
from datetime import datetime
import sqlite3
from config import my_token
from options_bot import forward_role_messages

mybot = telebot.TeleBot(my_token)  # your token


# mybot.get_chat(2022096545).linked_chat_id = -1001325934811
# mybot.get_chat(2022096545).type = "chanel"

@mybot.message_handler(commands=['start'])
def start(message):
    # mybot.send_message(message.chat.id,
    # "Здравсвуйте {0.first_name}! Здесь будут появлятся новости и сообщения!".format(
    #   message.from_user))
    mybot.send_message(message.chat.id, "Напишите пожалуйста свое имя и фамилию")
    mybot.register_next_step_handler(message, register_name)
    # mybot.get_chat(2022096545).linked_chat_id = -1001325934811
    # mybot.get_chat(2022096545).type = "chanel"


@mybot.message_handler(func=lambda message: True)
def echo(message):
    if message.text.lower() == '/help':
        mybot.send_message(message.chat.id, 'Данный бот создан учеником 10Б клaсса \n'
                                            'МБОУ "ГЮЛ №86" г.Ижевска '
                                            'Рахматуллиным Дамиром (@rahmatullinofficial) \n'
                                            'Учебный год 21/22 \n')
    elif message.text.lower == '/start':
        start()
    else:
        mybot.send_message(message.chat.id, "Извините, я Вас не понял, повторите еще раз \n"
                                            "Для обращения в поддержку бота -> /help")
    print(
        f'{message.from_user.username}: {message.text} -> '
        f'{datetime.utcfromtimestamp(message.date).strftime("%Y-%m-%d %H:%M:%S")}')


def register_name(message):
    name = message.text
    mybot.send_message(message.chat.id, "Спасибо! Здесь будет появлятся вся нужная для Вас информация!")
    new_user_add(message, name)


def new_user_add(message, name):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
          id INTEGER, teacher INTEGER, teacher_class INTEGER, mkinfmat INTEGER, mkn INTEGER, mkiy INTEGER, mkfil INTEGER,
          mken INTEGER, mkfot INTEGER, mki INTEGER, adm INTEGER, nick TEXT NOT NULL );
       """)
    db.commit()

    people_id = message.chat.id
    n = name  # go here
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
    forward_role_messages(message, "all")


mybot.polling(none_stop=True)
