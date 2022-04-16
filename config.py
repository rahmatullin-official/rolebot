from telebot import types

token = '2038672522:AAGYZPBVYnjvCKrFqCqXKafSEeQeC60nw70'
my_token = '2022096545:AAHmlx8cbNxQZSj1w_7XQkC7IYcsrp0WdRM'
mypass = "gul86"

button1 = "учитель"
button2 = "классный руководитель"
button3 = "администрация"
button4 = "мк"
button5 = "👤 пользователя"
button6 = "очистить 👤 пользователя"
button7 = "Назад"
button8 = "мк инф + матем"
button9 = "мк начальной школы"
button10 = "мк иностранные яз"
button111 = "мк филологи"
button12 = "мк естесвенные науки"
button13 = "мк физ-ра, ОБЖ, технолог"
button14 = "мк истории"
button15 = "кл 5"
button16 = "кл 6"
button17 = "кл 7"
button18 = "кл 8"
button19 = "кл 9"
button20 = "кл 10"
button21 = "кл 11"
button222 = "всем кл"
mk_boss = "руководитель мк"
button11 = "Выдать 👤"
button22 = "Действия с 👤"
button33 = "Обращения к 👤"
button44 = "Создать 📑"
button55 = "Отправить 🖼"

button0 = "всем"
help_commands = f'@adm роль -> {button3} \n' \
                f'@teacher роль -> {button1} \n' \
                f'@teacher_class роль -> {button2} \n' \
                f'@mkinfmat роль -> {button8} \n' \
                f'@mkn роль -> {button9} \n' \
                f'@mkiy роль -> {button10} \n' \
                f'@mkfil роль -> {button111} \n' \
                f'@mken роль -> {button12} \n' \
                f'@mkfot роль -> {button13} \n' \
                f'@mki роль -> {button14} \n' \
                f'для отправки сообщения -> message @role text \n' \
                f'для отправки сообщения нескольким ролям -> message @role @role2 text \n' \
                f'для просмотра id пользователей -> /users'
my_roles = ['adm', 'teacher', 'teacher_class', 'mkinfmat', 'mkn', 'mkiy', 'mkfil', 'mken', 'mkfot', 'mki', 'all',
            'mk_boss', 'tc5', 'tc6', 'tc7', 'tc8', 'tc9', 'tc10', 'tc11']
item0 = types.KeyboardButton(button0)
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
item15 = types.KeyboardButton(button15)
item16 = types.KeyboardButton(button16)
item17 = types.KeyboardButton(button17)
item18 = types.KeyboardButton(button18)
item19 = types.KeyboardButton(button19)
item20 = types.KeyboardButton(button20)
item21 = types.KeyboardButton(button21)
item22 = types.KeyboardButton(button22)
item33 = types.KeyboardButton(button33)
item44 = types.KeyboardButton(button44)
item55 = types.KeyboardButton(button55)
item222 = types.KeyboardButton(button222)
item_mkboss = types.KeyboardButton(mk_boss)
