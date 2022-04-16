import telebot
from telebot import types
from datetime import datetime
import sqlite3
import time

from config import my_token

mybot = telebot.TeleBot(my_token)  # your token

keys_for_chat = {
    'all': -1001606281501,
    'teacher': -1001690957601,
    'teacher_class': -1001686801828,
    'adm': -1001729571699,
    'mkinfmat': -1001511474725,
    'mkn': -1001658087867,
    'mkiy': -1001517694158,
    'mkfil': -1001635335948,
    'mken': -1001260170139,
    'mkfot': -1001609616531,
    'mki': -1001356109325,
    'tc5': -1001563191718,
    'tc6': -1001756242350,
    'tc7': -1001304608456,
    'tc8': -1001517360969,
    'tc9': -1001618046500,
    'tc10': -1001533803285,
    'tc11': -1001764058578,
    'mk_boss': -1001557273378,
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
    'mki': 'history_mki',
    'tc5': 'history_tc5',
    'tc6': 'history_tc6',
    'tc7': 'history_tc7',
    'tc8': 'history_tc8',
    'tc9': 'history_tc9',
    'tc10': 'history_tc10',
    'tc11': 'history_tc11',
    'mk_boss': 'history_mk_boss',
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
    mybot.send_message(message.chat.id, 'Данный бот создан учеником 10Б клaсса \n'
                                        'МБОУ "ГЮЛ №86" г.Ижевска \n'
                                        'Рахматуллиным Дамиром (@tatardami) \n'
                                        'Учебный год 21/22 \n')
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
            f"INSERT INTO users(id, teacher, teacher_class, mkinfmat, mkn, mkiy, mkfil, mken, mkfot, mki,"
            f" adm, nick, tc5, tc6, tc7, tc8, tc9, tc10, tc11, mk_boss) "
            f"VALUES ({people_id}, 0,0,0,0,0,0,0,0,0,0,'',0,0,0,0,0,0,0,0);")
        db.commit()
    sql.execute(f"UPDATE users SET nick=? WHERE id={message.chat.id};", [n])
    db.commit()
    # forward_role_messages_mybot(message, "all")


while True:
    try:
        mybot.polling(none_stop=False)
        time.sleep(0.3)
    except Exception as e:
        print(e)
        time.sleep(15)
