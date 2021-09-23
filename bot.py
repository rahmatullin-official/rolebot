import telebot
from telebot import types
import sqlite3
from config import token, item1, item2, item3, item4, item5, item6, button1, button2, button3, button4, button5, button6

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     "Здравсвуйте {0.first_name}! Выберите пожалуйста свою роль".format(message.from_user),
                     reply_markup=markup)
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
       id INTEGER, teacher INTEGER, teacher_class INTEGER, mk INTEGER, administration INTEGER);
    """)
    db.commit()

    people_id = message.chat.id
    sql.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = sql.fetchone()
    if data:
        pass
    else:
        sql.execute(f"INSERT INTO users(id, teacher, teacher_class, mk, administration) VALUES ({people_id}, 0,0,0,0);")
        db.commit()


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == button1:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET teacher = 1 WHERE id = {message.chat.id}')
            db.commit()
            bot.send_message(message.chat.id, f'Вам присовенна роль - {button1}')
        elif message.text == button2:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET teacher_class = 1 WHERE id = {message.chat.id}')
            db.commit()
            bot.send_message(message.chat.id, f'Вам присвоенна роль - {button2}')
        elif message.text == button3:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET administration = 1 WHERE id = {message.chat.id}')
            db.commit()
            bot.send_message(message.chat.id, f'Вам присвоеена роль - {button3}')
        elif message.text == button4:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mk = 1 WHERE id = {message.chat.id}')
            db.commit()
            bot.send_message(message.chat.id, f'Вам присвоенна роль - {button4}')
        elif message.text == button5:
            cnt = 0
            output = ''
            some_roles = ['учитель', 'классный руководитель', 'мк', 'администрация']
            my_roles = []
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'SELECT teacher,teacher_class,mk,administration FROM users WHERE id = {message.chat.id}')
            for i in sql.fetchall():
                for j in i:
                    my_roles.append(j)
            for i in my_roles:
                if i == 1:
                    output += f'{some_roles[cnt]}, '
                cnt += 1
            if len(output) == 0:
                bot.send_message(message.chat.id, f'У вас еще нет ролей')
            else:
                bot.send_message(message.chat.id, f'Ваши роли: {output[0:-2]}')
        elif message.text == button6:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'UPDATE users SET teacher = 0,teacher_class = 0,mk = 0,administration = 0 WHERE id = {message.chat.id}'
            )
            db.commit()
            bot.send_message(message.chat.id, 'Ваши роли успешно очищенны!')


def add_user_role(role):
    if role == button1:
        # cursor.execute("INSERT INTO login_id VALUES(?);", role)
        pass


bot.polling(none_stop=True)