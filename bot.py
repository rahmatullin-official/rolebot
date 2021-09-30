import telebot
from telebot import types
import sqlite3
from config import token, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item111, item12, \
    item13, item14, item11, item22, item33, item44, button1, button2, button3, \
    button4, button5, button6, button11, button22, button33, button44, button7, button8, button9, button10, button111, \
    button12, \
    button13, button14, help_commands, my_roles, my_token

bot = telebot.TeleBot(token)
bot2 = telebot.TeleBot(my_token)
opt = 0
cnt = 0
my_messages = []
question = ""
role_option = ''
roles = []
my_id = []
user_id = ""


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(item11, item22, item44, item33)

    bot.send_message(message.chat.id,
                     "Здравсвуйте {0.first_name}!".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global my_messages, my_id
    try:
        global opt
        text = message.text
        print(f'OPT: {opt}')
        if opt > 0:
            if message.text == '/stop':
                opt = 0
                send_poll(message, my_messages)
            else:
                if my_id[0] == message.chat.id:
                    my_messages.append(text)
        print(my_messages)
        bot_message(message)
    except Exception as ex:
        bot.send_message(message.chat.id, str(ex))
        my_messages = []
        my_id = []


@bot.message_handler(content_types=['text'])
def bot_message(message):
    global my_id, user_id, cnt
    if message.chat.type == 'private':
        if message.text == button11 or message.text == button1 or message.text == button2 or message.text == button3 \
                or message.text == button4 or message.text == button7 or message.text == button8 \
                or message.text == button9 or message.text == button10 or message.text == button111 \
                or message.text == button12 or message.text == button13 or message.text == button14:
            if message.text == button11:
                send = bot.send_message(message.chat.id, 'Напишите id человека, которому хотите выдать роль!')
                bot.register_next_step_handler(send, users_role)
                print(user_id)
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
                send = bot.send_message(message.chat.id, 'Напишите id человека, роль которого хотите посмотреть!')
                bot.register_next_step_handler(send, sr)
            elif message.text == button6:
                send = bot.send_message(message.chat.id, 'Напишите id человека, роли которого хотите очистить!')
                bot.register_next_step_handler(send, сr)
            elif message.text == button7:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(item11, item22, item33)
                bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
        elif message.text == button33 or message.text == '/help_commands':
            bot.send_message(message.chat.id, help_commands)
        elif message.text == button44:
            if len(my_id) == 0 or my_id[0] == message.chat.id:
                my_id.append(message.chat.id)
                bot.send_message(message.chat.id, "Напишите тему опроса!")
                bot.register_next_step_handler(message, create_question_poll)
            else:
                bot.send_message(message.chat.id, 'Другой пользователь уже создает опрос! Пожалуйста подождите.')
        elif message.text[:7].lower() == 'message':
            check_user_role(message)
        elif message.text == '/users':
            view_users(message)


def add_user_role(role, message):
    if role == button1:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET teacher = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button1}')
    elif role == button2:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET teacher_class = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button2}')
    elif role == button3:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET adm = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button3}')
    elif role == button8:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkinfmat = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button8}')
    elif role == button9:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkn = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button9}')
    elif role == button10:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkiy = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button10}')
    elif role == button111:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkfil = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button111}')
    elif role == button12:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mken = 1 WHERE id = {user_id}')
        db.commit()
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button12}')
    elif role == button13:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mkfot = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button13}')
    elif role == button14:
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(f'UPDATE users SET mki = 1 WHERE id = {user_id}')
        db.commit()
        bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button14}')
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
        f'SELECT teacher,teacher_class,mkinfmat, mkn, mkiy, mkfil, mken, mkfot, mki,adm FROM users WHERE id = {user_id}')
    for i in sql.fetchall():
        for j in i:
            my_roles.append(j)
    for i in my_roles:
        if i == 1:
            output += f'{some_roles[cnt]}, '
        cnt += 1
    if len(output) == 0:
        bot.send_message(message.chat.id, f'У пользователя еще нет ролей')
    else:
        bot.send_message(message.chat.id, f'Роли пользователя: {output[0:-2]}')


def clear_my_roles(message):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    sql.execute(
        f'UPDATE users SET teacher = 0,teacher_class = 0,mkinfmat = 0, mkn = 0, mkiy = 0, mkfil = 0, mken = 0, mkfot = 0,'
        f' mki = 0,adm = 0 WHERE id = {user_id}'
    )
    db.commit()
    bot.send_message(message.chat.id, 'Роли пользователя успешно очищенны!')


def check_user_role(message):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    users_users = []
    some_roles = message.text.split()[1:]
    some_roles = [i.replace('@', '') for i in some_roles]
    message_roles = [i for i in some_roles if i in my_roles]
    if len(message_roles) == 0:
        bot.send_message(message.chat.id, 'Вы неверно указали роль\n'
                                          'Для вызова списка ролей напишите /help_commands')
    else:
        find_message = message.text.rfind(message_roles[-1]) + len(message_roles[-1]) + 1
        for i in message_roles:
            sql.execute(
                f'SELECT id FROM users WHERE {i} = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
        for i in users_users:
            bot2.send_message(i, message.text[find_message:])


def create_question_poll(message):
    global question
    question = message.text
    if question == '/stop':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню')
    else:
        bot.send_message(message.chat.id, 'Напишите для какой роли/ей вы хотите создать опрос (@role)')
        bot.send_message(message.chat.id, 'Для перечисления ролей используйте пробел (@role1 @role2)')
        bot.register_next_step_handler(message, role_for_option)
    print(question)


def send_poll(message, messages):
    global my_messages, roles, my_id
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    users_roles = []
    for i in roles:
        db_roles = sql.execute(
            f'SELECT id FROM users WHERE {i} = 1'
        )
        for z in sql.fetchall():
            for j in z:
                users_roles.append(j)
    bot2.send_poll(users_roles[0], question, messages, False)
    mm = bot2.send_poll(users_roles[0], question, messages, False).message_id
    if len(users_roles) > 1:
        for i in users_roles[1:]:
            bot2.forward_message(i, users_roles[0], mm)
    my_messages = []
    my_id = []


def role_for_option(message):
    global opt, role_option, roles, my_id
    role_option = message.text.split()
    count_roles = [i for i in role_option if '@' in i]
    roles = [i.replace('@', '') for i in role_option]
    print(roles)
    if len(count_roles) == 1:
        if roles[0] not in my_roles:
            bot.send_message(message.chat.id,
                             'Вы указали неверную роль! Чтобы посмотреть список ролей -> /help_commands')
        else:
            bot.send_message(message.chat.id, 'Чтобы закончить писать пункты опроса напишите /stop')
            opt += 1
    else:
        not_roles = len([i for i in roles if i not in my_roles])
        if not_roles != 0:
            if not_roles == 1:
                bot.send_message(message.chat.id,
                                 f'Вы указали {not_roles} неверную роль! Чтобы посмотреть список ролей -> /help_commands')
            else:
                bot.send_message(message.chat.id,
                                 f'Вы указали {not_roles} неверных роли! Чтобы посмотреть список ролей -> /help_commands')
        else:
            bot.send_message(message.chat.id, 'Чтобы закончить писать пункты опроса напишите /stop')
            opt += 1


def role_commands(message):
    bot.send_message(message.chat.id, help_commands)


def view_users(message):
    db = sqlite3.connect('all_users.db')
    sql = db.cursor()
    ms = ''
    sql.execute(
        f'SELECT id, nick FROM users'
    )
    for i in sql.fetchall():
        ms += f'user nickname: {i[1]} user id: {i[0]} \n'
    bot.send_message(message.chat.id, ms)


def users_role(message):
    global user_id, cnt
    user_id = message.text
    create_keyboard(message)


def sr(message):
    global user_id, cnt
    user_id = message.text
    show_my_roles(message)


def сr(message):
    global user_id, cnt
    user_id = message.text
    clear_my_roles(message)


def create_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3, item4, item7)
    bot.send_message(message.chat.id,
                     "{0.first_name}, выберите пожалуйста роль пользователя".format(message.from_user),
                     reply_markup=markup)


bot.polling(none_stop=True)
