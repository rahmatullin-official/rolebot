import telebot
from telebot import types
import sqlite3
from config import token, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item111, item12, \
    item13, item14, item11, item22, item33, item44, button1, button2, button3, \
    button4, button5, button6, button11, button22, button33, button44, button7, button8, button9, button10, button111, \
    button12, \
    button13, button14, help_commands

bot = telebot.TeleBot(token)
opt = 0
my_messages = []
question = ""
role_option = ''


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(item11, item22, item44, item33)

    bot.send_message(message.chat.id,
                     "Здравсвуйте {0.first_name}!".format(message.from_user),
                     reply_markup=markup)
    new_user_add(message)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global opt
    text = message.text
    print(f'OPT: {opt}')
    if opt > 0:
        if message.text == '/stop':
            opt = 0
            send_poll(message, my_messages)
        else:
            my_messages.append(text)
    print(my_messages)
    bot_message(message)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == button11 or message.text == button1 or message.text == button2 or message.text == button3 \
                or message.text == button4 or message.text == button7 or message.text == button8 \
                or message.text == button9 or message.text == button10 or message.text == button111 \
                or message.text == button12 or message.text == button13 or message.text == button14:
            if message.text == button11:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(item1, item2, item3, item4, item7)
                bot.send_message(message.chat.id,
                                 "{0.first_name}, выберите пожалуйста свою роль".format(message.from_user),
                                 reply_markup=markup)
            elif message.text == button1:
                add_user_role(button1, message)
            elif message.text == button2:
                add_user_role(button2, message)
            elif message.text == button3:
                add_user_role(button3, message)
            elif message.text == button4 or message.text == button8 or message.text == button9 \
                    or message.text == button10 or message.text == button111 or message.text == button12 \
                    or message.text == button13 or message.text == button14:
                if message.text == button4:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    markup.add(item8, item9, item10, item111, item12, item13, item14, item7)
                    bot.send_message(message.chat.id,
                                     "{0.first_name}, выберите пожалуйста категорию мк".format(message.from_user),
                                     reply_markup=markup)
                elif message.text == button8:
                    add_user_role(button8, message)
                elif message.text == button9:
                    add_user_role(button9, message)
                elif message.text == button10:
                    add_user_role(button10, message)
                elif message.text == button111:
                    add_user_role(button111, message)
                elif message.text == button12:
                    add_user_role(button12, message)
                elif message.text == button13:
                    add_user_role(button13, message)
                elif message.text == button14:
                    add_user_role(button14, message)
            elif message.text == button7:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(item11, item22, item44, item33)
                bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
        elif message.text == button22 or message.text == button6 or message.text == button5 or message.text == button7:
            if message.text == button22:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(item5, item6, item7)
                bot.send_message(message.chat.id,
                                 "{0.first_name}, выберите действие".format(message.from_user),
                                 reply_markup=markup)
            elif message.text == button5:
                show_my_roles(message)
            elif message.text == button6:
                clear_my_roles(message)
            elif message.text == button7:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(item11, item22, item33)
                bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
        elif message.text == button33:
            bot.send_message(message.chat.id, help_commands)
        elif message.text == button44:
            bot.send_message(message.chat.id, "Напишите тему опроса!")
            bot.register_next_step_handler(message, create_question_poll)
        elif message.text[:8].lower() == '@teacher' and message.text[8] == ' ':
            check_user_role(button1, message)
        elif message.text[:14].lower() == '@teacher_class':
            check_user_role(button2, message)
        elif message.text[:4].lower() == '@adm':
            check_user_role(button3, message)
        elif message.text[:9].lower() == '@mkinfmat':
            check_user_role(button8, message)
        elif message.text[:4].lower() == '@mkn':
            check_user_role(button9, message)
        elif message.text[:5].lower() == '@mkiy':
            check_user_role(button10, message)
        elif message.text[:6].lower() == '@mkfil':
            check_user_role(button111, message)
        elif message.text[:5].lower() == '@mken':
            check_user_role(button12, message)
        elif message.text[:6].lower() == '@mkfot':
            check_user_role(button13, message)
        elif message.text[:4].lower() == '@mki':
            check_user_role(button14, message)


def new_user_add(message):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
          id INTEGER, teacher INTEGER, teacher_class INTEGER, mkinfmat INTEGER, mkn INTEGER, mkiy INTEGER, mkfil INTEGER,
          mken INTEGER, mkfot INTEGER, mki INTEGER, adm INTEGER);
       """)
    db.commit()

    people_id = message.chat.id
    sql.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = sql.fetchone()
    if data:
        pass
    else:
        sql.execute(
            f"INSERT INTO users(id, teacher, teacher_class, mkinfmat, mkn, mkiy, mkfil, mken, mkfot, mki, adm) VALUES ({people_id}, 0,0,0,0,0,0,0,0,0,0);")
        db.commit()


def add_user_role(role, message):
    if role == button1:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET teacher = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присовенна роль - {button1}')
    elif role == button2:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET teacher_class = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоенна роль - {button2}')
    elif role == button3:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET adm = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоеена роль - {button3}')
    elif role == button8:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkinfmat = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоеена роль - {button8}')
    elif role == button9:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkn = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоеена роль - {button9}')
    elif role == button10:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkiy = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоеена роль - {button10}')
    elif role == button111:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkfil = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоеена роль - {button111}')
    elif role == button12:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mken = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоеена роль - {button12}')
    elif role == button13:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkfot = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоеена роль - {button13}')
    elif role == button14:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mki = 1 WHERE id = {message.chat.id}')
        db.commit()
        bot.send_message(message.chat.id, f'Вам присвоеена роль - {button14}')
    # elif role == button4:
    #     db = sqlite3.connect('all_users.db')
    #     sql = db.cursor()
    #     sql.execute(f'UPDATE users SET mk = 1 WHERE id = {message.chat.id}')
    #     db.commit()
    #     bot.send_message(message.chat.id, f'Вам присвоенна роль - {button4}')


def show_my_roles(message):
    cnt = 0
    output = ''
    some_roles = ['учитель', 'классный руководитель', 'мк инф + матем', 'мк начальной школы', 'мк иностранные яз',
                  'мк филологи', 'мк естесвенные науки',
                  'мк физ-ра, ОБЖ, технолог', 'мк истории', 'администрация']
    my_roles = []
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    sql.execute(
        f'SELECT teacher,teacher_class,mkinfmat, mkn, mkiy, mkfil, mken, mkfot, mki,adm FROM users WHERE id = {message.chat.id}')
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


def clear_my_roles(message):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    sql.execute(
        f'UPDATE users SET teacher = 0,teacher_class = 0,mkinfmat = 0, mkn = 0, mkiy = 0, mkfil = 0, mken = 0, mkfot = 0,'
        f' mki = 0,adm = 0 WHERE id = {message.chat.id}'
    )
    db.commit()
    bot.send_message(message.chat.id, 'Ваши роли успешно очищенны!')


def check_user_role(role, message):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    if role == button1:
        teacher_users = []
        sql.execute(
            f'SELECT id FROM users WHERE teacher = 1'
        )
        for i in sql.fetchall():
            for j in i:
                teacher_users.append(j)
        for i in teacher_users:
            bot.send_message(i, message.text[9:])
    elif role == button2:
        teacher_class_users = []
        sql.execute(
            f'SELECT id FROM users WHERE teacher_class = 1'
        )
        for i in sql.fetchall():
            for j in i:
                teacher_class_users.append(j)
        for i in teacher_class_users:
            bot.send_message(i, message.text[15:])
    elif role == button3:
        administration_users = []
        sql.execute(
            f'SELECT id FROM users WHERE adm = 1'
        )
        for i in sql.fetchall():
            for j in i:
                administration_users.append(j)
        for i in administration_users:
            bot.send_message(i, message.text[5:])
    elif role == button8:
        mkinfmat_users = []
        sql.execute(
            f'SELECT id FROM users WHERE mkinfmat = 1'
        )
        for i in sql.fetchall():
            for j in i:
                mkinfmat_users.append(j)
        for i in mkinfmat_users:
            bot.send_message(i, message.text[9:])
    elif role == button9:
        mkn_users = []
        sql.execute(
            f'SELECT id FROM users WHERE mkn = 1'
        )
        for i in sql.fetchall():
            for j in i:
                mkn_users.append(j)
        for i in mkn_users:
            bot.send_message(i, message.text[5:])
    elif role == button10:
        mkiy_users = []
        sql.execute(
            f'SELECT id FROM users WHERE mkiy = 1'
        )
        for i in sql.fetchall():
            for j in i:
                mkiy_users.append(j)
        for i in mkiy_users:
            bot.send_message(i, message.text[6:])
    elif role == button111:
        mkfil_users = []
        sql.execute(
            f'SELECT id FROM users WHERE mkfil = 1'
        )
        for i in sql.fetchall():
            for j in i:
                mkfil_users.append(j)
        for i in mkfil_users:
            bot.send_message(i, message.text[7:])
    elif role == button12:
        mken_users = []
        sql.execute(
            f'SELECT id FROM users WHERE mken = 1'
        )
        for i in sql.fetchall():
            for j in i:
                mken_users.append(j)
        for i in mken_users:
            bot.send_message(i, message.text[6:])
    elif role == button13:
        mkfot_users = []
        sql.execute(
            f'SELECT id FROM users WHERE mkfot = 1'
        )
        for i in sql.fetchall():
            for j in i:
                mkfot_users.append(j)
        for i in mkfot_users:
            bot.send_message(i, message.text[7:])
    elif role == button14:
        mki_users = []
        sql.execute(
            f'SELECT id FROM users WHERE mki = 1'
        )
        for i in sql.fetchall():
            for j in i:
                mki_users.append(j)
        for i in mki_users:
            bot.send_message(i, message.text[5:])


def create_question_poll(message):
    global question
    question = message.text
    bot.send_message(message.chat.id, 'Напишите для какой роли вы хотите создать опрос (@role)')
    bot.register_next_step_handler(message, role_for_option)
    print(question)


def send_poll(message, my_messages):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    users_roles = []
    roles = sql.execute(
        f'SELECT id FROM users WHERE {role_option[1:]} = 1'
    )
    for i in sql.fetchall():
        for j in i:
            users_roles.append(j)
    for i in users_roles:
        bot.send_poll(i, question, my_messages, False)


def role_for_option(message):
    global opt, role_option
    role_option = message.text
    bot.send_message(message.chat.id, 'Чтобы закончить писать пункты опроса напишите /stop')
    opt += 1


bot.polling(none_stop=True)
