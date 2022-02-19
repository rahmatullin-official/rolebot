import telebot
from telebot import types
from datetime import datetime
import sqlite3

from config import my_token

mybot = telebot.TeleBot(my_token)  # your token

keys_for_chat = {
    'all': "yourchatnumber",
    'teacher': "yourchatnumber",
    'teacher_class': "yourchatnumber",
    'adm': "yourchatnumber",
    'mkinfmat': "yourchatnumber",
    'mkn': "yourchatnumber",
    'mkiy': "yourchatnumber",
    'mkfil': "yourchatnumber",
    'mken': "yourchatnumber",
    'mkfot': "yourchatnumber",
    'mki': "yourchatnumber",
}
history_upd = {
    'all': 'history_all',
    'teacher': 'history_teacher',
    'teacher_class': 'history_teacher_class',
    'adm': 'history_adm',
    'mkinfmat': 'history_mkinfmat',
    'mkn': 'history_mkn',
    'mkiy': 'history_mkiy',
    'mkfil': 'history_mkfil',
    'mken': 'history_mken',
    'mkfot': 'history_mkfot',
    'mki': 'history_mki'
}


@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id, "Напишите пожалуйста свое имя и фамилию")
    mybot.register_next_step_handler(message, register_name)


@mybot.message_handler(func=lambda message: True)
def echo(message):
    if message.text.lower() == '/help':
        mybot.send_message(message.chat.id, 'Данный бот создан учеником 10Б клaсса \n'
                                            'МБОУ "ГЮЛ №86" г.Ижевска \n'
                                            'Рахматуллиным Дамиром (@tatardami) \n'
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


def forward_role_messages_mybot(message, role):
    messages_list = []
    db = sqlite3.connect('history_roles.db')
    sql = db.cursor()
    sql.execute(f'SELECT id FROM {history_upd[role]}')
    for z in sql.fetchall():
        for j in z:
            messages_list.append(j)
    for i in messages_list:
        mybot.forward_message(message.chat.id, keys_for_chat[role], i)


def new_user_add(message, name):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
          id INTEGER, teacher INTEGER, teacher_class INTEGER, mkinfmat INTEGER, mkn INTEGER, mkiy INTEGER, mkfil INTEGER,
          mken INTEGER, mkfot INTEGER, mki INTEGER, adm INTEGER, nick TEXT NOT NULL );
       """)
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
    forward_role_messages_mybot(message, "all")


mybot.polling(none_stop=True)
