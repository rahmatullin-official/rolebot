import os
import telebot
from telebot import types
import sqlite3
from datetime import datetime
from config import *
import time

# bot tokens
bot = telebot.TeleBot(token)
bot2 = telebot.TeleBot(my_token)

# global values for some operations xd
opt = 0
cnt = 0
my_messages = []
question = ""
role_option = ''
roles = []
my_id = []
user_id = ""
role = ""
old_roles = []

# global values to add history messages to roles
# history_messages_all = []
# history_messages_teacher = []
# history_messages_teacher_class = []
# history_messages_adm = []
# history_messages_mkinfmat = []
# history_messages_mkn = []
# history_messages_mkiy = []
# history_messages_mkfil = []
# history_messages_mken = []
# history_messages_mkfot = []
# history_messages_mki = []

# keys for chat and history upd
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

try:
    @bot.message_handler(commands=['start'])
    def start(message):
        send = bot.send_message(message.chat.id, 'Для продолжения введите пароль!')
        bot.register_next_step_handler(send, loggin)


    @bot.message_handler(content_types=['photo'])
    def what_photo(message):
        global role, history_messages_all, history_messages_mki, history_messages_mkfot, \
            history_messages_mkiy, history_messages_mkn, history_messages_mken, history_messages_mkfil, \
            history_messages_adm, history_messages_mkinfmat, history_messages_teacher, \
            history_messages_teacher_classs, keys_for_chat
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
        src = 'C:/Users/Администратор/Desktop/rolebot_beta/images/' + file_info.file_path[7:]
        # src = 'D:/PythonProjects/rolebot' + file_info.file_path[7:]
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            chat_id = 0
            # if len(message_roles) == 0:
            #   bot.send_message(message.chat.id, 'Вы неверно указали роль\n'
            #                                    'Для вызова списка ролей напишите /help_commands')
            # find_message = message.caption.rfind(message_roles[-1]) + len(message_roles[-1]) + 1
            if message_roles[0] == "all":
                with open(src, "rb") as file:
                    sql.execute(
                        f'SELECT id FROM users'
                    )
                    chat_id = -1001606281501
                    mm = bot2.send_photo(chat_id, file).message_id
                    for z in sql.fetchall():
                        for j in z:
                            users_users.append(j)
                    for i in users_users:
                        bot2.forward_message(i, chat_id, mm)
                    update_history('all', mm)
            else:
                with open(src, "rb") as file:
                    for i in message_roles:
                        chat_id = keys_for_chat[i]
                        mm = bot2.send_photo(chat_id, file).message_id
                        sql.execute(
                            f'SELECT id FROM users WHERE {i} = 1'
                        )
                        for z in sql.fetchall():
                            for j in z:
                                users_users.append(j)
                    for i in users_users:
                        bot2.forward_message(i, chat_id, mm)
                    if keys_for_chat['teacher'] == chat_id:
                        update_history('teacher', mm)
                    elif keys_for_chat['teacher_class'] == chat_id:
                        update_history('teacher_class', mm)
                    elif keys_for_chat['adm'] == chat_id:
                        update_history('adm', mm)
                    elif keys_for_chat['mkinfmat'] == chat_id:
                        update_history('mkinfmat', mm)
                    elif keys_for_chat['mkn'] == chat_id:
                        update_history('mkn', mm)
                    elif keys_for_chat['mkiy'] == chat_id:
                        update_history('mkiy', mm)
                    elif keys_for_chat['mkfil'] == chat_id:
                        update_history('mkfil', mm)
                    elif keys_for_chat['mken'] == chat_id:
                        update_history('mken', mm)
                    elif keys_for_chat['mkfot'] == chat_id:
                        update_history('mkfot', mm)
                    elif keys_for_chat['mki'] == chat_id:
                        update_history('mki', mm)
                    elif keys_for_chat['tc5'] == chat_id:
                        update_history('tc5', mm)
                    elif keys_for_chat['tc6'] == chat_id:
                        update_history('tc6', mm)
                    elif keys_for_chat['tc7'] == chat_id:
                        update_history('tc7', mm)
                    elif keys_for_chat['tc8'] == chat_id:
                        update_history('tc8', mm)
                    elif keys_for_chat['tc9'] == chat_id:
                        update_history('tc9', mm)
                    elif keys_for_chat['tc10'] == chat_id:
                        update_history('tc10', mm)
                    elif keys_for_chat['tc11'] == chat_id:
                        update_history('tc11', mm)
                    elif keys_for_chat['mk_boss'] == chat_id:
                        update_history('mk_boss', mm)

                        # bot2.send_photo(i, file)
                        # message.caption[find_message:]
            bot.send_message(message.chat.id, 'Картинка была успешно отправленна пользователям!')
            # os.remove(src)


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
                    or message.text == button12 or message.text == button13 or message.text == button14 or message.text == button15 \
                    or message.text == button16 or message.text == button17 or message.text == button18 or message.text == button19 \
                    or message.text == button20 or message.text == button21 or message.text == mk_boss:
                if message.text == button11:
                    send = bot.send_message(message.chat.id, 'Напишите id человека, которому хотите выдать роль!')
                    bot.register_next_step_handler(send, users_role)
                    # print(user_id)
                elif message.text == button1:
                    add_user_role(button1, message)
                elif message.text == button2:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    markup.add(item15, item16, item17, item18, item19, item20, item21, item7)
                    bot.send_message(message.chat.id,
                                     "{0.first_name}, выберите пожалуйста параллель".format(message.from_user),
                                     reply_markup=markup)
                elif message.text == button3:
                    add_user_role(button3, message)
                elif message.text == button4 or message.text == button8 or message.text == button9 \
                        or message.text == button10 or message.text == button111 or message.text == button12 \
                        or message.text == button13 or message.text == button14:
                    if message.text == button4:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        markup.add(item8, item9, item10, item111, item12, item13, item14, item_mkboss, item7)
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
                elif message.text == button15:
                    add_user_role(button15, message)
                elif message.text == button16:
                    add_user_role(button16, message)
                elif message.text == button17:
                    add_user_role(button17, message)
                elif message.text == button18:
                    add_user_role(button18, message)
                elif message.text == button19:
                    add_user_role(button19, message)
                elif message.text == button20:
                    add_user_role(button20, message)
                elif message.text == button21:
                    add_user_role(button21, message)
                elif message.text == mk_boss:
                    add_user_role(mk_boss, message)
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
            forward_role_messages(message, "teacher")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button1}')
        # elif role == button2:
        #     db = sqlite3.connect('all_users.db')
        #     sql = db.cursor()
        #     sql.execute(f'UPDATE users SET teacher_class = 1 WHERE id = {user_id}')
        #     forward_role_messages(message, "teacher_class")
        #     db.commit()
        #     bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button2}')
        elif role == button3:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET adm = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "adm")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button3}')
        elif role == button8:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mkinfmat = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "mkinfmat")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button8}')
        elif role == button9:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mkn = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "mkn")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button9}')
        elif role == button10:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mkiy = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "mkiy")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button10}')
        elif role == button111:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mkfil = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "mfil")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button111}')
        elif role == button12:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mken = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "mken")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button12}')
        elif role == button13:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mkfot = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "mkfot")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button13}')
        elif role == button14:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mki = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "mki")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button14}')
        elif role == button15:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET tc5 = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "tc5")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button15}')
        elif role == button16:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET tc6 = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "tc6")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button16}')
        elif role == button17:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET tc7 = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "tc7")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button17}')
        elif role == button18:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET tc8 = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "tc8")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button18}')
        elif role == button19:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET tc9 = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "tc9")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button19}')
        elif role == button20:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET tc10 = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "tc10")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button20}')
        elif role == button21:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET tc11 = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "tc11")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {button21}')
        elif role == mk_boss:
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(f'UPDATE users SET mk_boss = 1 WHERE id = {user_id}')
            db.commit()
            forward_role_messages(message, "mk_boss")
            bot.send_message(message.chat.id, f'Пользователю присвоена роль - {mk_boss}')
        # elif role == button4:
        #     db = sqlite3.connect('all_users.db')
        #     sql = db.cursor()
        #     sql.execute(f'UPDATE users SET mk = 1 WHERE id = {message.chat.id}')
        #     db.commit()
        #     bot.send_message(message.chat.id, f'Вам присвоенна роль - {button4}')


    def show_my_roles(message):
        try:
            cnt = 0
            output = ''
            some_roles = ['учитель', 'классный руководитель', 'мк инф + матем', 'мк начальной школы',
                          'мк иностранные яз',
                          'мк филологи', 'мк естесвенные науки',
                          'мк физ-ра, ОБЖ, технолог', 'мк истории', 'администрация', 'классный руководитель5',
                          'классный руководитель6', 'классный руководитель7',
                          'классный руководитель8', 'классный руководитель9', 'классный руководитель10',
                          'классный руководитель11', 'руководитель мк']
            my_roles = []
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT teacher,teacher_class,mkinfmat, mkn, mkiy, mkfil, mken, mkfot, mki,adm, tc5, tc6, tc7, tc8, tc9, tc10'
                f',tc11, mk_boss FROM users WHERE id = {user_id}')
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
                cnt = 0
        except Exception as ex:
            bot.send_message(message.chat.id, f"Произошла ошибка: {ex}, повторите пожалуйста попытку")


    def clear_my_roles(message):
        db = sqlite3.connect('all_users.db')
        sql = db.cursor()
        sql.execute(
            f'UPDATE users SET teacher = 0,teacher_class = 0,mkinfmat = 0, mkn = 0, mkiy = 0, mkfil = 0, mken = 0, mkfot = 0, tc5 = 0,'
            f' mki = 0,adm = 0, tc6 = 0, tc7 = 0, tc8 = 0, tc9 = 0, tc10 = 0, tc11 = 0, mk_boss = 0 WHERE id = {user_id}'
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
            chat_id = -1001606281501
            for z in sql.fetchall():
                for j in z:
                    users_roles.append(j)
            mm = bot2.send_poll(chat_id, question, messages, False).message_id
            history_messages_all.append(mm)
            if len(users_roles) > 1:
                for i in users_roles[1:]:
                    bot2.forward_message(i, chat_id, mm)
            my_messages = []
            my_id = []
        else:
            chat_id = 0
            for i in roles:
                chat_id = keys_for_chat[i]
                db_roles = sql.execute(
                    f'SELECT id FROM users WHERE {i} = 1'
                )
                for z in sql.fetchall():
                    for j in z:
                        users_roles.append(j)
            mm = bot2.send_poll(chat_id, question, messages, False).message_id
            if len(users_roles) > 1:
                for i in users_roles[1:]:
                    bot2.forward_message(i, chat_id, mm)
            if keys_for_chat['teacher'] == chat_id:
                update_history('teacher', mm)
            elif keys_for_chat['teacher_class'] == chat_id:
                update_history('teacher_class', mm)
            elif keys_for_chat['adm'] == chat_id:
                update_history('adm', mm)
            elif keys_for_chat['mkinfmat'] == chat_id:
                update_history('mkinfmat', mm)
            elif keys_for_chat['mkn'] == chat_id:
                update_history('mkn', mm)
            elif keys_for_chat['mkiy'] == chat_id:
                update_history('mkiy', mm)
            elif keys_for_chat['mkfil'] == chat_id:
                update_history('mkfil', mm)
            elif keys_for_chat['mken'] == chat_id:
                update_history('mken', mm)
            elif keys_for_chat['mkfot'] == chat_id:
                update_history('mkfot', mm)
            elif keys_for_chat['mki'] == chat_id:
                update_history('mki', mm)
            elif keys_for_chat['tc5'] == chat_id:
                update_history('tc5', mm)
            elif keys_for_chat['tc6'] == chat_id:
                update_history('tc6', mm)
            elif keys_for_chat['tc7'] == chat_id:
                update_history('tcc7', mm)
            elif keys_for_chat['tc8'] == chat_id:
                update_history('tc8', mm)
            elif keys_for_chat['tc9'] == chat_id:
                update_history('tc9', mm)
            elif keys_for_chat['tc10'] == chat_id:
                update_history('tc10', mm)
            elif keys_for_chat['tc11'] == chat_id:
                update_history('tc11', mm)
            elif keys_for_chat['mk_boss'] == chat_id:
                update_history('mk_boss', mm)

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
            if len(ms) < 4050:
                ms += f'user nickname: {i[1]} user id: {i[0]} \n'
                print(len(ms))
            else:
                bot.send_message(message.chat.id, ms)
                ms = ''
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
        # my_role = role
        users_users = []
        if role == "@all":
            chat_id = -1001606281501
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users'
            )
            mm = bot2.send_message(chat_id, my_message).message_id
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("all", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@teacher":
            chat_id = -1001690957601
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE teacher = 1'
            )
            mm = bot2.send_message(chat_id, my_message).message_id
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("teacher", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@teacher_class":
            chat_id = -1001686801828
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE teacher_class = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("teacher_class", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@adm":
            chat_id = -1001729571699
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE adm = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("adm", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkinfmat".lower():
            chat_id = -1001511474725
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkinfmat = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("mkinfmat", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkn":
            chat_id = -1001658087867
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkn = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("mkn", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkiy":
            chat_id = -1001517694158
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkiy = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("mkiy", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkfil":
            chat_id = -1001635335948
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkfil = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("mkfil", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mken":
            chat_id = -1001260170139
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mken = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("mken", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mkfot":
            chat_id = -1001609616531
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mkfot = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("mkfot", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mki":
            chat_id = -1001356109325
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mki = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("mki", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@tc5":
            chat_id = keys_for_chat['tc5']
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE tc5 = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("tc5", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@tc6":
            chat_id = keys_for_chat['tc6']
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE tc6 = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("tc6", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@tc7":
            chat_id = keys_for_chat['tc7']
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE tc7 = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("tc7", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@tc8":
            chat_id = keys_for_chat['tc8']
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE tc8 = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("tc8", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@tc9":
            chat_id = keys_for_chat['tc9']
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE tc9 = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("tc9", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@tc10":
            chat_id = keys_for_chat['tc10']
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE tc10 = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("tc10", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@tc11":
            chat_id = keys_for_chat['tc11']
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE tc11 = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("tc11", mm)
            bot.send_message(message.chat.id, f'Сообщение успешно отправленно пользователям!')
        elif role == "@mk_boss":
            chat_id = keys_for_chat['mk_boss']
            mm = bot2.send_message(chat_id, my_message).message_id
            db = sqlite3.connect('all_users.db')
            sql = db.cursor()
            sql.execute(
                f'SELECT id FROM users WHERE mk_boss = 1'
            )
            for z in sql.fetchall():
                for j in z:
                    users_users.append(j)
            for i in users_users:
                bot2.forward_message(i, chat_id, mm)
            update_history("mk_boss", mm)
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
        elif message.text == mk_boss:
            role = "@mk_boss"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)


    def teacher_class_check_photo(message):
        global role
        if message.text == button15:
            role = "tc5"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button16:
            role = "tc6"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button17:
            role = "tc7"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button18:
            role = "tc8"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button19:
            role = "tc9"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button20:
            role = "tc10"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button21:
            role = "tc11"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button222:
            role = "teacher_class"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
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
        elif message.text == mk_boss:
            role = "mk_boss"
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
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item15, item16, item17, item18, item19, item20, item21, item222, item7)
            bot.send_message(message.chat.id,
                             "{0.first_name}, выберите пожалуйста параллель".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, teacher_class_check)
            # role = "@teacher_class"
            # bot.send_message(message.chat.id, "Напишите нужный текст")
            # bot.register_next_step_handler(message, last_message)
        elif message.text == "администрация":
            role = "@adm"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item8, item9, item10, item111, item12, item13, item14, mk_boss, item7)
            bot.send_message(message.chat.id,
                             "{0.first_name}, выберите пожалуйста категорию мк".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, mk_check_message)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
        print(message.text)


    def teacher_class_check_option(message):
        global role
        if message.text == button15:
            role = "tc5"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button16:
            role = "tc6"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button17:
            role = "tc7"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button18:
            role = "tc8"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button19:
            role = "tc9"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button20:
            role = "tc10"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button21:
            role = "tc11"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)


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
        elif message.text == mk_boss:
            role = "mk_boss"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item11, item22, item33, item44, item55)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)


    def teacher_class_check(message):
        global role
        if message.text == button15:
            role = "@tc5"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button16:
            role = "@tc6"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button17:
            role = "@tc7"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button18:
            role = "@tc8"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button19:
            role = "@tc9"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button20:
            role = "@tc10"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button21:
            role = "@tc11"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
        elif message.text == button222:
            role = "@teacher_class"
            bot.send_message(message.chat.id, "Напишите нужный текст")
            bot.register_next_step_handler(message, last_message)
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
            bot.register_next_step_handler(message, teacher_class_check_option)
            # bot.register_next_step_handler(message, role_for_option)
        elif message.text == "администрация":
            role = "adm"
            bot.register_next_step_handler(message, role_for_option)
        elif message.text == button4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item8, item9, item10, item111, item12, item13, item14, mk_boss, item7)
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
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item15, item16, item17, item18, item19, item20, item21, item7)
            bot.send_message(message.chat.id,
                             "{0.first_name}, выберите пожалуйста категорию мк".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, teacher_class_check_photo)
        elif message.text == "администрация":
            role = "adm"
            bot.send_message(message.chat.id, "Отправте нужную фотографию")
        elif message.text == button4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(item8, item9, item10, item111, item12, item13, item14, mk_boss, item7)
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


    def forward_role_messages(message, role):
        pass
        # global old_roles
        # messages_list = []
        # db = sqlite3.connect('history_roles.db')
        # sql = db.cursor()
        # sql.execute(f'SELECT id FROM {history_upd[role]}')
        # for z in sql.fetchall():
        #     for j in z:
        #         messages_list.append(j)
        # for i in messages_list:
        #     bot2.forward_message(message.chat.id, keys_for_chat[role], i)


    def update_history(role, mm):
        db = sqlite3.connect('history_roles.db')
        sql = db.cursor()
        sql.execute(f"""INSERT INTO {history_upd[role]}(id) VALUES ({mm});""")
        db.commit()
        print("db updated")


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

while True:
    try:
        bot.polling(none_stop=False)
        time.sleep(0.3)
    except Exception as e:
        print(e)
        time.sleep(15)
