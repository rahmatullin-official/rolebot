from telebot import types

token = ""  # your token
button1 = "учитель"
button2 = "классный руководитель"
button3 = "администрация"
button4 = "мк"
button5 = "мои роли"
button6 = "очистить роли"
button7 = "Назад"
button11 = "получить роль"
button22 = "действия с ролями"
button33 = "команды для оповещений"
help_commands = '@adm text - отправить сообщение людям с ролью "администратор" \n' \
                '@teach text - отправить сообщение людям с ролью "учитель" \n' \
                '@teacher_class text - отправить сообщение людям с ролью "классный руководитель"'
item1 = types.KeyboardButton(button1)
item2 = types.KeyboardButton(button2)
item3 = types.KeyboardButton(button3)
item4 = types.KeyboardButton(button4)
item5 = types.KeyboardButton(button5)
item6 = types.KeyboardButton(button6)
item7 = types.KeyboardButton(button7)
item11 = types.KeyboardButton(button11)
item22 = types.KeyboardButton(button22)
item33 = types.KeyboardButton(button33)
