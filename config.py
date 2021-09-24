from telebot import types

token = ""  # your token
button1 = "учитель"
button2 = "классный руководитель"
button3 = "администрация"
button4 = "мк"
button5 = "мои роли"
button6 = "очистить роли"
button7 = "Назад"
button8 = "мк инф + матем"
button9 = "мк начальной школы"
button10 = "мк иностранные яз"
button111 = "мк филологи"
button12 = "мк естесвенные науки"
button13 = "мк физ-ра, ОБЖ, технолог"
button14 = "мк истории"
button11 = "получить роль"
button22 = "действия с ролями"
button33 = "команды для оповещений"
button44 = "создать опрос"
help_commands = f'@adm text - отправить сообщение людям с ролью {button3} \n' \
                f'@teacher text - отправить сообщение людям с ролью {button1} \n' \
                f'@teacher_class text - отправить сообщение людям с ролью {button2} \n' \
                f'@mkinfmat text - отправить сообщение люядм с ролью {button8} \n' \
                f'@mkn text - отправить сообщение людям с ролью {button9} \n' \
                f'@mkiy text - отправить сообщение людям с ролью {button10} \n' \
                f'@mkfil text - отправить сообщение людям с ролью {button111} \n' \
                f'@mken text - отправить сообщение людям с ролью {button12} \n' \
                f'@mkfot text - отправить сообщение людям с ролью {button13} \n' \
                f'@mki text - отправить сообщение людям с ролью {button14}'
item1 = types.KeyboardButton(button1)
item2 = types.KeyboardButton(button2)
item3 = types.KeyboardButton(button3)
item4 = types.KeyboardButton(button4)
item5 = types.KeyboardButton(button5)
item6 = types.KeyboardButton(button6)
item7 = types.KeyboardButton(button7)
item8 = types.KeyboardButton(button8)
item9 = types.KeyboardButton(button9)
item10 = types.KeyboardButton(button10)
item111 = types.KeyboardButton(button111)
item12 = types.KeyboardButton(button12)
item13 = types.KeyboardButton(button13)
item14 = types.KeyboardButton(button14)
item11 = types.KeyboardButton(button11)
item22 = types.KeyboardButton(button22)
item33 = types.KeyboardButton(button33)
item44 = types.KeyboardButton(button44)
