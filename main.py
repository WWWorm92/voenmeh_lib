import telebot
from telebot import types
import datetime

# Создаем экземпляр бота
bot = telebot.TeleBot('6128509852:AAHtAYWFyXbeOlKWRTuAn551gP2CTheKw1c')

# Создаем клавиатурный лейаут
keyboard_layout_1 = types.InlineKeyboardMarkup(row_width=2)
keyboard_layout_1.add(types.InlineKeyboardButton('Режим работы', callback_data='departments_shedule'),
                      types.InlineKeyboardButton('Читальные залы', callback_data='reading_halls'),
                      types.InlineKeyboardButton('Контакты', callback_data='contacts'),
                      types.InlineKeyboardButton('Как взять литературу?', callback_data='how_to_1'),
                      types.InlineKeyboardButton('Как получить читательский билет?', callback_data='how_to_2')
                      )
keyboard_layout_1.add(types.InlineKeyboardButton('-> 2', callback_data='next_1'))
keyboard_layout_2 = types.InlineKeyboardMarkup(row_width=2)
keyboard_layout_2.add(
    types.InlineKeyboardButton('Как воспользоваться библиотечными системами из дома?', callback_data='how_to_3'),
    types.InlineKeyboardButton('Режим работы отделов сервисных услуг и секции организации выставок',
                               callback_data='service_shedule'),
    types.InlineKeyboardButton('Сколько стоит распечатка/копирование?', callback_data='price'),
    types.InlineKeyboardButton('Как оплатить утерянную книгу?', callback_data='how_to_4'),
    types.InlineKeyboardButton('Как узнать на какой срок выдана книга?', callback_data='how_to_5')
)
keyboard_layout_2.add(types.InlineKeyboardButton('1 <-', callback_data='back_2'),
                      types.InlineKeyboardButton('-> 3', callback_data='next_2'))
keyboard_layout_3 = types.InlineKeyboardMarkup(row_width=2)
keyboard_layout_3.add(types.InlineKeyboardButton('Как продлить литературу?', callback_data='how_to_6'),
                      types.InlineKeyboardButton('Как подписать обходной лист?', callback_data='how_to_7'),
                      )
keyboard_layout_3.add(types.InlineKeyboardButton('2 <-', callback_data='back_3'))

current_keyboard = 1


# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    global current_keyboard
    # Получаем имя пользователя из объекта message
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    # Отправляем приветственное сообщение с использованием имени пользователя
    bot.send_message(message.chat.id, f"Привет, {first_name} {last_name}! Что тебя интересует?",
                     reply_markup=keyboard_layout_1)


# Обработчик для кнопок
@bot.callback_query_handler(func=lambda call: True)
def button_handler(call):
    # Получаем текст кнопки из объекта call
    text = call.data
    # Отвечаем на вопрос пользователя
    if text == 'departments_shedule':
        bot.send_message(call.message.chat.id,
                         '- Абонемент младших курсов АМК: ПН – ПТ 9:00 – 19:00, перерыв с 12:00 до 12:30\n'
                         '- Абонемент старших курсов АСК: ПН – ПТ 9:00 – 19:00, СБ 10:00 – 15:00, перерыв с 12:00 до 12:30\n'
                         '- Абонемент художественной литературы: ПН – ПТ 9:00 – 17:00, перерыв с 12:00 до 12:30\n'
                         '- Абонемент литературы на иностранных языках и языкознания: ПН – ЧТ 10:00 – 18:00, ПТ 10:00 – 17:00, перерыв с 12:00 до 12:30\n'
                         '- Абонемент общественно-политической литературы: ПН – ЧТ 9:00 – 17:00, ПТ 9:00 – 16:00, перерыв с 12:00 до 12:30\n'
                         '- Отдел комплектования: ПН – ПТ 9:00 – 17:00, перерыв 12:00 – 12:30\n'
                         '- Информационно-библиографический отдел ПН – ПТ 9:00 – 17:00, перерыв 12:00 – 12:30\n'
                         '- Отдел сервисных услуг и сектор организации выставок ПН – ПТ 9:00 – 17:00, перерыв 12:00 – 12:30')
    elif text == 'reading_halls':
        bot.send_message(call.message.chat.id, 'Режим работы читальных залов:\n'
                                               '- Главный корпус 3 этаж: ПН – ПТ 9:00 – 19:00, СБ 9:00 – 15:00\n'
                                               '- Главный корпус 4 этаж (школа): ПН – ПТ 11:00 – 19:00\n'
                                               '- УЛК 2 этаж: ПН – ПТ 9:00 – 19:00')
    elif text == 'contacts':
        bot.send_message(call.message.chat.id, '- Директор библиотеки Сессина Н.В. +7(812)490-05-86\n'
                                               '- Зам.директора Перепеч С.Б. +7(812)495-76-84\n'
                                               '- Отдел научной литературы  +7(812)495-76-56\n'
                                               '- Отдел учебной литературы в Главном корпусе +7(812)495-76-97\n'
                                               '- Отдел учебной литературы в УЛК +7(812)490-05-39')
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
                         'Для получения литературы необходимо иметь читательский билет.', parse_mode='Markdown')
    elif text == 'how_to_2':
        bot.send_message(call.message.chat.id,
                         'Читательский билет можно получить в библиотеке главного корпуса на 3 этаже.\n'
                         'С собой достаточно иметь пропуск.')
    elif text == 'how_to_3':
        bot.send_message(call.message.chat.id, '........Отправить пдф со всеми э-библиотечными системами.......\n')
    elif text == 'service_shedule':
        bot.send_message(call.message.chat.id, 'Режим работы отделов сервисных услуг и секции организации выставок:\n''
                                               '- Главный корпус 3 этаж: ПН – ЧТ 9:00 – 17:00, ПТ 10:00 – 17:00, перерыв с 12:00 до 12:30\n'
                                               '- Новый корпус 2 этаж: ПН – ЧТ 9:00 – 17:00, ПТ 10:00 – 17:00, перерыв с 12:00 до 12:30')
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
                                               'В продаже также имеются канцтовары и книги.')
    elif text == 'how_to_4':
        bot.send_message(call.message.chat.id,
                         'В случае утери книги необходимо прийти в отдел комплектования (Главный корпус 3 этаж дверь перед абонементом), '
                         'где вам посчитают стоимость утерянной книги и объяснят дальнейшие действия.')
    elif text == 'how_to_5':
        bot.send_message(call.message.chat.id,
                         'В личном кабинете после авторизации можно посмотреть, какие книги у вас есть и на какой срок.')
    elif text == 'how_to_6':
        bot.send_message(call.message.chat.id,
                         'Достаточно прийти с читательским билетом на абонемент, где была заимствована книга и библиограф продлит книгу на семестр. '
                         'Книги фундаментального отдела выдаются на 2 месяца.')
    elif text == 'how_to_7':
        bot.send_message(call.message.chat.id,
                         'Обходной лист подписывается в библиотеке Главного корпуса. '
                         'еобходимо сдать все книги и читательский билет (при утере билета оплачивается штраф в размере 50 руб).')


# Запускаем бота
bot.polling(none_stop=True)
