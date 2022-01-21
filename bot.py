import os
import telebot
from telebot import types
import sqlite3
from datetime import datetime
from config import *

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
role = ""

try:
    @bot.message_handler(commands=['start'])
    def start(message):
        send = bot.send_message(message.chat.id, 'Для продолжения введите пароль!')
        bot.register_next_step_handler(send, loggin)


    @bot.message_handler(content_types=['photo'])
    def what_photo(message):
        global role
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        users_users = []
        message_roles = []
        # try:
        #     if len(str(message.text)) != 0 and len(str(message.caption)) != 0:
        #         some_roles = message.caption.split()[1:]
        #         some_roles = [i.replace('@', '') for i in some_roles]
        #         message_roles = [i for i in some_roles if i in my_roles]
        #     else:
        #         message_roles = [].append(role)
        #         role = ""
        # except TypeError:
        message_roles.append(role)
        role = ""
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'D:/bot' + file_info.file_path[7:]
        # src = 'D:/PythonProjects/rolebot' + file_info.file_path[7:]
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            # if len(message_roles) == 0:
            #   bot.send_message(message.chat.id, 'Вы неверно указали роль\n'
            #                                    'Для вызова списка ролей напишите /help_commands')
            # find_message = message.caption.rfind(message_roles[-1]) + len(message_roles[-1]) + 1
            if message_roles[0] == "all":
                sql.execute(
                    f'SELECT id FROM users'
                )
                for z in sql.fetchall():
                    for j in z:
                        users_users.append(j)
                for i in users_users:
                    with open(src, "rb") as file:
                        bot2.send_photo(i, file)  # ,message.caption[find_message:]
            else:
                for i in message_roles:
                    sql.execute(
                        f'SELECT id FROM users WHERE {i} = 1'
                    )
                    for z in sql.fetchall():
                        for j in z:
                            users_users.append(j)
                for i in users_users:
                    with open(src, "rb") as file:
                        bot2.send_photo(i, file)  # ,message.caption[find_message:]
        bot.send_message(message.chat.id, 'Картинка была успешно отправленна пользователям!')
        os.remove(src)


    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        global my_messages, my_id
        try:
            global opt
            text = message.text
            # print(f'OPT: {opt}')
            print(
                f'{message.from_user.username}: {message.text} -> '
                f'{datetime.utcfromtimestamp(message.date).strftime("%Y-%m-%d %H:%M:%S")}')
            if opt > 0:
                if message.text == '/stop':
                    opt = 0
                    send_poll(message, my_messages)
                else:
                    if my_id[0] == message.chat.id:
                        my_messages.append(text)
            # print(my_messages)
            bot_message(message)
        except Exception as ex:
            bot.send_message(message.chat.id, str(ex))
            my_messages = []
            my_id = []


    @bot.message_handler(content_types=['text'])
    def bot_message(message):
        global my_id, user_id, cnt, role
        if message.chat.type == 'private':
            if message.text == button11 or message.text == button1 or message.text == button2 or message.text == button3 \
                    or message.text == button4 or message.text == button7 or message.text == button8 \
                    or message.text == button9 or message.text == button10 or message.text == button111 \
                    or message.text == button12 or message.text == button13 or message.text == button14:
                if message.text == button11:
                    send = bot.send_message(message.chat.id, 'Напишите id человека, которому хотите выдать роль!')
                    bot.register_next_step_handler(send, users_role)
                    # print(user_id)
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
                    markup.add(item11, item22, item44, item33, item55)
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
            elif message.text == '/help_commands':
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
            elif message.text[:15] == '/python_command':
                python_command(message)
            elif message.text == button33:
                message_with_keyboard(message)
            elif message.text == button55:
                photo_keyboard(message)


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
            # bot.send_message(message.chat.id, 'Напишите для какой роли/ей вы хотите создать опрос (@role)')
            # bot.send_message(message.chat.id, 'Для перечисления ролей используйте пробел (@role1 @role2)')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item1, item2, item3, item4, item0, item7)
            bot.send_message(message.chat.id,
                             "Выберите роль",
                             reply_markup=markup)
            if message.text == button7:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(item11, item22, item33, item44, item55)
                bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
            else:
                bot.register_next_step_handler(message, what_user_option)
        # print(question)


    def send_poll(message, messages):
        global my_messages, roles, my_id
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        users_roles = []
        if roles[0] == "all":
            db_roles = sql.execute(
                f'SELECT id FROM users'
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
        else:
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
        global opt, role_option, roles, my_id, role
        # role_option = message.text.split()
        # count_roles = [i for i in role_option if '@' in i]
        # roles = [i.replace('@', '') for i in role_option]
        count_roles = []
        count_roles.append(role)
        roles.append(role)
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


    def loggin(message):
        password = message.text
        if password == mypass:
            log_in(message)
        else:
            bot.send_message(message.chat.id, 'Пароль не верный')
            start(message)


    def log_in(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(item11, item22, item44, item55, item33)

        bot.send_message(message.chat.id,
                         "Здравсвуйте {0.first_name}!".format(message.from_user),
                         reply_markup=markup)


    def create_keyboard(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(item1, item2, item3, item4, item7)
        bot.send_message(message.chat.id,
                         "{0.first_name}, выберите пожалуйста роль пользователя".format(message.from_user),
                         reply_markup=markup)


    def python_command(message):
        answer = message.text[16:]
        try:
            try:
                exec(answer)
            except Exception as e:
                print(e)
                try:
                    bot.send_message(message.chat.id, e)
                except:
                    pass
        except:
            try:
                bot.send_message(message.chat.id, "Произошла ошибка во время выполненя кода")
            except:
                pass


    def send_user_message(message):
        global role
        my_message = message.text
        my_role = role
        users_users = []
        if role == "@all":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@teacher":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE teacher = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@teacher_class":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE teacher_class = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@adm":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE adm = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkinfmat".lower():
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkinfmat = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkn":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkn = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkiy":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkiy = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkfil":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkfil = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mken":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mken = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkfot":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkfot = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mki":
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mki = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.send_message(i, message.text)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')


    def last_message(message):
        send_user_message(message)


    def mk_check_message(message):
        global role
        if message.text == button8:
            role = "@mkinfmat"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button9:
            role = "@mkn"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button10:
            role = "@mkiy"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button111:
            role = "@mkfil"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button12:
            role = "@mken"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button13:
            role = "@mkfot"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button14:
            role = "@mki"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)


    def mk_check_photo(message):
        global role
        if message.text == button8:
            role = "mkinfmat"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button9:
            role = "mkn"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button10:
            role = "mkiy"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button111:
            role = "mkfil"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button12:
            role = "mken"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button13:
            role = "mkfot"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button14:
            role = "mki"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)


    def what_role(message):
        global role
        if message.text == "всем":
            role = "@all"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == "учитель":
            role = "@teacher"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == "классный руководитель":
            role = "@teacher_class"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == "администрация":
            role = "@adm"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item8, item9, item10, item111, item12, item13, item14, item7)
            bot.send_message(message.chat.id,
                             "{0.first_name}, выберите пожалуйста категорию мк".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, mk_check_message)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
        print(message.text)


    def mk_check_option(message):
        global role
        if message.text == button8:
            role = "mkinfmat"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button9:
            role = "mkn"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button10:
            role = "mkiy"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button111:
            role = "mkfil"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button12:
            role = "mken"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button13:
            role = "mkfot"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button14:
            role = "mki"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)


    def what_user_option(message):
        global role
        if message.text == "всем":
            role = "all"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == "учитель":
            role = "teacher"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == "классный руководитель":
            role = "teacher_class"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == "администрация":
            role = "adm"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item8, item9, item10, item111, item12, item13, item14, item7)
            bot.send_message(message.chat.id,
                             "{0.first_name}, выберите пожалуйста категорию мк".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, mk_check_option)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)


    def what_user_photo(message):
        global role
        if message.text == "всем":
            role = "all"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == "учитель":
            role = "teacher"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == "классный руководитель":
            role = "teacher_class"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == "администрация":
            role = "adm"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item8, item9, item10, item111, item12, item13, item14, item7)
            bot.send_message(message.chat.id,
                             "{0.first_name}, выберите пожалуйста категорию мк".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, mk_check_photo)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)


    def photo_keyboard(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(item1, item2, item3, item4, item0, item7)
        bot.send_message(message.chat.id,
                         "Выберите роль",
                         reply_markup=markup)
        if message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
        else:
            bot.register_next_step_handler(message, what_user_photo)


    @bot.message_handler(content_types=['text'])
    def message_with_keyboard(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(item1, item2, item3, item4, item0, item7)
        bot.send_message(message.chat.id,
                         "Выберите роль",
                         reply_markup=markup)
        if message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
        else:
            bot.register_next_step_handler(message, what_role)
        print(message.text)
except Exception as ex:
    print(ex)

bot.polling(none_stop=True)
