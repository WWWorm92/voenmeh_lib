import telebot
from telebot import types
import datetime

current_keyboard = 0
lib_1=''
lib_2=''
lib_3=''
lib_4=''
lib_5=''
lib_6=''
rh_1=''
rh_2=''
rh_3=''
rh_4=''

# Создаем экземпляр бота
bot = telebot.TeleBot('6128509852:AAHtAYWFyXbeOlKWRTuAn551gP2CTheKw1c')

# Создаем клавиатурный лейаут
keyboard_layout_1 = types.InlineKeyboardMarkup(row_width=1)
keyboard_layout_1.add(types.InlineKeyboardButton('Режим работы', callback_data='departments_shedule'),
                      types.InlineKeyboardButton('Режим работы отделов сервисных услуг',
                               callback_data='service_shedule'),
                      types.InlineKeyboardButton('Читальные залы', callback_data='reading_halls'),
                      types.InlineKeyboardButton('Контакты', callback_data='contacts'),
                      types.InlineKeyboardButton('Сколько стоит распечатка/копирование?', callback_data='price')
                      )
keyboard_layout_1.add(types.InlineKeyboardButton('➡', callback_data='next_1'))
keyboard_layout_2 = types.InlineKeyboardMarkup(row_width=1)
keyboard_layout_2.add(
    types.InlineKeyboardButton('Как получить читательский билет?', callback_data='how_to_2'),
    types.InlineKeyboardButton('Как воспользоваться библиотечными системами из дома?', callback_data='how_to_3'),
    types.InlineKeyboardButton('Как взять литературу?', callback_data='how_to_1'),
    types.InlineKeyboardButton('Как оплатить утерянную книгу?', callback_data='how_to_4'),
    types.InlineKeyboardButton('Как узнать на какой срок выдана книга?', callback_data='how_to_5')
)
keyboard_layout_2.add(types.InlineKeyboardButton('⬅', callback_data='back_2'),
                      types.InlineKeyboardButton('➡', callback_data='next_2'))
keyboard_layout_3 = types.InlineKeyboardMarkup(row_width=1)
keyboard_layout_3.add(types.InlineKeyboardButton('Как продлить литературу?', callback_data='how_to_6'),
                      types.InlineKeyboardButton('Как подписать обходной лист?', callback_data='how_to_7'),
                      )
keyboard_layout_3.add(types.InlineKeyboardButton('⬅', callback_data='back_3'))
keyboard_delete = telebot.types.InlineKeyboardMarkup()
delete_button = telebot.types.InlineKeyboardButton(text='Удалить', callback_data='delete_message')
keyboard_delete.add(delete_button)


def is_library_open(department='AMK'):
    global lib_1,lib_2,lib_3,lib_4,lib_5,lib_6,rh_1,rh_2,rh_3,rh_4
    o='✅СЕЙЧАС ОТКРЫТО✅'
    c='🚫СЕЙЧАС ЗАКРЫТО🚫'
    now = datetime.datetime.now()
    weekday = now.weekday()  # Возвращает день недели от 0 (понедельник) до 6 (воскресенье)
    time = now.time()
    if department == 'AMK':
        if weekday in range(0, 5):  # Работаем с понедельника по пятницу
            if time >= datetime.time(9, 0) and time <= datetime.time(19, 0) and not (
                    time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                           30)):  # Библиотека открыта с 9 до 19, перерыв с 12 до 12:30
                lib_1 = o
            else:
                lib_1 = c
        else:  # Выходной день
            lib_1 = c
    elif department == 'ASK':
        if weekday in range(0, 6):  # Работаем с понедельника по субботу
            if weekday == 5:  # Суббота
                if time >= datetime.time(10, 0) and time <= datetime.time(15, 0) and not (
                        time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                               30)):  # Библиотека открыта с 10 до 15, перерыв с 12 до 12:30
                    lib_2 = o
                else:
                    lib_2 = c
            else:
                if time >= datetime.time(9, 0) and time <= datetime.time(19, 0) and not (
                        time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                               30)):  # Библиотека открыта с 9 до 19, перерыв с 12 до 12:30
                    lib_2 = o
                else:
                    lib_2 = c
        else:  # Выходной день
            lib_2 = c
    elif department == 'AHL':
        if weekday in range(0, 5):  # Работаем с понедельника по пятницу
            if time >= datetime.time(9, 0) and time <= datetime.time(17, 0) and not (
                    time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                           30)):  # Библиотека открыта с 9 до 17, перерыв с 12 до 12:30
                lib_3 = o
            else:
                lib_3 = c
        else:  # Выходной день
            lib_3 = c
    elif department == 'ALI':
        if weekday in range(0, 4):  # Работаем с понедельника по четверг
            if time >= datetime.time(10, 0) and time <= datetime.time(18, 0) and not (
                    time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                           30)):  # Библиотека открыта с 10 до 18, перерыв с 12 до 12:30
                lib_4 = o
            else:
                lib_4 = c
        elif weekday == 4:  # Пятница
            if time >= datetime.time(10, 0) and time <= datetime.time(17, 0) and not (
                    time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                           30)):  # Библиотека открыта с 10 до 17, перерыв с 12 до 12:30
                lib_4 = o
            else:
                lib_4 = c
        else:  # Выходной день
            lib_4 = c
    if department == 'AOPL':
        if weekday in range(0, 4):  # Работаем с понедельника по четверг
            if time >= datetime.time(9, 0) and time <= datetime.time(17, 0) and not (
                    time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                           30)):  # Абонемент открыт с 9 до 17, перерыв с 12 до 12:30
                lib_5 = o
            else:
                lib_5 = c
        elif weekday == 4:  # Пятница
            if time >= datetime.time(9, 0) and time <= datetime.time(16, 0) and not (
                    time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                           30)):  # Абонемент открыт с 9 до 16, перерыв с 12 до 12:30
                lib_5 = o
            else:
                lib_5 = c
        else:  # Выходной день
            lib_5 = c
    elif department == 'OK' or department == 'IBO' or department == 'OSSOV':
        if weekday in range(0, 5):  # Работаем с понедельника по пятницу
            if time >= datetime.time(9, 0) and time <= datetime.time(17, 0) and not (
                    time >= datetime.time(12, 0) and time <= datetime.time(12,
                                                                           30)):  # Отдел открыт с 9 до 17, перерыв с 12 до 12:30
                lib_6 = o
            else:
                lib_6 = c
        else:  # Выходной день
            lib_6 = c
    if department == 'GK3':
        if weekday in range(0, 5):  # Работаем с понедельника по пятницу
            if time >= datetime.time(9, 0) and time <= datetime.time(19, 0):  # Библиотека открыта с 9 до 19
                rh_1=o
            else:
                rh_2=c
        elif weekday == 5:  # Суббота
            if time >= datetime.time(9, 0) and time <= datetime.time(15, 0):  # Библиотека открыта с 9 до 15
                rh_1=o
            else:
                rh_1=c
        else:  # Выходной день
            rh_1=c
    elif department == 'GK4':
        if weekday in range(0, 5):  # Работаем с понедельника по пятницу
            if time >= datetime.time(11, 0) and time <= datetime.time(19, 0):  # Библиотека открыта с 11 до 19
                rh_2=o
            else:
                rh_2=c
        else:  # Выходной день
            rh_2=c
    elif department == 'ULK2':
        if weekday in range(0, 5):  # Работаем с понедельника по пятницу
            if time >= datetime.time(9, 0) and time <= datetime.time(19, 0):  # Библиотека открыта с 9 до 19
                rh_3=o
            else:
                rh_3=c
        else:  # Выходной день
            rh_3=c
    if department == 'GK3N':
        if weekday in range(0, 4):    # Работаем с понедельника по четверг
            if time >= datetime.time(9, 0) and time < datetime.time(12, 0):    # Библиотека открыта с 9 до 12
                rh_4=o
            elif time >= datetime.time(12, 30) and time <= datetime.time(17, 0):    # Библиотека открыта с 12:30 до 17
                rh_4=o
            else:
                rh_4=c
        elif weekday == 4:    # Пятница
            if time >= datetime.time(10, 0) and time < datetime.time(12, 0):    # Библиотека открыта с 10 до 12
                rh_4=o
            elif time >= datetime.time(12, 30) and time <= datetime.time(17, 0):    # Библиотека открыта с 12:30 до 17
                rh_4=o
            else:
                rh_4=c
        else:    # Выходной день
            rh_4=c


# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    global current_keyboard
    # Получаем имя пользователя из объекта message
    first_name = message.from_user.first_name
    # last_name = message.from_user.last_name
    # Отправляем приветственное сообщение с использованием имени пользователя
    bot.send_message(message.chat.id, f"Привет, {first_name}! Что тебя интересует?",
                     reply_markup=keyboard_layout_1)


# Обработчик для кнопок
@bot.callback_query_handler(func=lambda call: True)
def button_handler(call):
    is_library_open('AMK')
    is_library_open('ASK')
    is_library_open('AHL')
    is_library_open('ALI')
    is_library_open('AOPL')
    is_library_open('OK')
    is_library_open('GK3')
    is_library_open('GK4')
    is_library_open('ULK2')
    is_library_open('GK3N')
    if call.data == 'delete_message':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # Получаем текст кнопки из объекта call
    text = call.data
    # Отвечаем на вопрос пользователя
    if text == 'departments_shedule':
        bot.send_message(call.message.chat.id,
                         '- Абонемент младших курсов АМК: ПН – ПТ 9:00 – 19:00, перерыв с 12:00 до 12:30 \n'+lib_1+'\n\n'
                         '- Абонемент старших курсов АСК: ПН – ПТ 9:00 – 19:00, СБ 10:00 – 15:00, перерыв с 12:00 до 12:30 \n'+lib_2+'\n\n'
                         '- Абонемент художественной литературы: ПН – ПТ 9:00 – 17:00, перерыв с 12:00 до 12:30 \n'+lib_3+'\n\n'
                         '- Абонемент литературы на иностранных языках и языкознания: ПН – ЧТ 10:00 – 18:00, ПТ 10:00 – 17:00, перерыв с 12:00 до 12:30 \n'+lib_4+'\n\n'
                         '- Абонемент общественно-политической литературы: ПН – ЧТ 9:00 – 17:00, ПТ 9:00 – 16:00, перерыв с 12:00 до 12:30\n '+lib_5+'\n\n'
                         '- Отдел комплектования: ПН – ПТ 9:00 – 17:00, перерыв 12:00 – 12:30 \n'+lib_6+'\n\n'
                         '- Информационно-библиографический отдел ПН – ПТ 9:00 – 17:00, перерыв 12:00 – 12:30\n '+lib_6+'\n\n'
                         '- Отдел сервисных услуг и сектор организации выставок ПН – ПТ 9:00 – 17:00, перерыв 12:00 – 12:30\n '+lib_6,
                         reply_markup=keyboard_delete
                         )
    elif text == 'reading_halls':
        bot.send_message(call.message.chat.id, 'Режим работы читальных залов:\n'
                                               '- Главный корпус 3 этаж: ПН – ПТ 9:00 – 19:00, СБ 9:00 – 15:00\n'+rh_1+'\n\n'
                                               '- Главный корпус 4 этаж (школа): ПН – ПТ 11:00 – 19:00\n'+rh_2+'\n\n'
                                               '- УЛК 2 этаж: ПН – ПТ 9:00 – 19:00\n'+rh_3, reply_markup=keyboard_delete)

    elif text == 'contacts':
        bot.send_message(call.message.chat.id, '- Директор библиотеки Сессина Н.В. +7(812)490-05-86\n'
                                               '- Зам.директора Перепеч С.Б. +7(812)495-76-84\n'
                                               '- Отдел научной литературы  +7(812)495-76-56\n'
                                               '- Отдел учебной литературы в Главном корпусе +7(812)495-76-97\n'
                                               '- Отдел учебной литературы в УЛК +7(812)490-05-39',
                         reply_markup=keyboard_delete)
    elif text == 'how_to_1':
        bot.send_message(call.message.chat.id,
                         'Книгу в печатном формате можно получить на абонементах, заполнив заявочный лист.\n'
                         'В заявочном листе необходимо указать:\n'
                         ' -Шифр книги\n'
                         ' -Автора\n'
                         ' -Заглавие\n'
                         ' -Том\n'
                         ' -Год издания\n'
                         'Вся информация содержится в [эл.каталоге](ya.ru)\n\n'
                         'Для получения литературы необходимо иметь читательский билет.', parse_mode='Markdown',
                         reply_markup=keyboard_delete)
    elif text == 'how_to_2':
        bot.send_message(call.message.chat.id,
                         'Читательский билет можно получить в библиотеке главного корпуса на 3 этаже.\n'
                         'С собой достаточно иметь пропуск.', reply_markup=keyboard_delete)
    elif text == 'how_to_3':
        bot.send_message(call.message.chat.id,
                         'https://telegra.ph/Rekomendacii-po-ispolzovaniyu-biblioteki-Voenmeha-03-25\n',
                         reply_markup=keyboard_delete)
    elif text == 'service_shedule':
        bot.send_message(call.message.chat.id, 'Режим работы отделов сервисных услуг и секции организации выставок:\n'
                                               '- Главный корпус 3 этаж: ПН – ЧТ 9:00 – 17:00, ПТ 10:00 – 17:00, перерыв с 12:00 до 12:30\n'+rh_4+'\n\n'
                                               '- Новый корпус 2 этаж: ПН – ЧТ 9:00 – 17:00, ПТ 10:00 – 17:00, перерыв с 12:00 до 12:30\n'+rh_4,
                         reply_markup=keyboard_delete)
    elif text == 'price':
        bot.send_message(call.message.chat.id, 'Черно-белая печать:\n'
                                               'А4 – 5р.\n'
                                               'А3 – 15р.\n'
                                               'А2 – 50р.\n'
                                               'А1 – 80р.\n'
                                               'За одну страницу\n\n'
                                               'Черно-белое копирование:\n'
                                               'А4 – 5р.\n'
                                               'А3 – 10р.\n'
                                               'за одну страницу\n\n'
                                               'Сканирование – 10р.\n\n'
                                               'В продаже также имеются канцтовары и книги.',
                         reply_markup=keyboard_delete)
    elif text == 'how_to_4':
        bot.send_message(call.message.chat.id,
                         'В случае утери книги необходимо прийти в отдел комплектования (Главный корпус 3 этаж дверь перед абонементом), '
                         'где вам посчитают стоимость утерянной книги и объяснят дальнейшие действия.',
                         reply_markup=keyboard_delete)
    elif text == 'how_to_5':
        bot.send_message(call.message.chat.id,
                         'В личном кабинете после авторизации можно посмотреть, какие книги у вас есть и на какой срок.',
                         reply_markup=keyboard_delete)
    elif text == 'how_to_6':
        bot.send_message(call.message.chat.id,
                         'Достаточно прийти с читательским билетом на абонемент, где была заимствована книга и библиограф продлит книгу на семестр. '
                         'Книги фундаментального отдела выдаются на 2 месяца.', reply_markup=keyboard_delete)
    elif text == 'how_to_7':
        bot.send_message(call.message.chat.id,
                         'Обходной лист подписывается в библиотеке Главного корпуса. '
                         'Необходимо сдать все книги и читательский билет (при утере билета оплачивается штраф в размере 50 руб).',
                         reply_markup=keyboard_delete)
    elif text == 'next_1':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, f"=Страница 2=",
                         reply_markup=keyboard_layout_2)
    elif text == 'back_2':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, f"=Страница 1=",
                         reply_markup=keyboard_layout_1)
    elif text == 'next_2':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, f"=Страница 3=",
                         reply_markup=keyboard_layout_3)
    elif text == 'back_3':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, f"=Страница 2=",
                         reply_markup=keyboard_layout_2)


# Запускаем бота
bot.polling(none_stop=True)
