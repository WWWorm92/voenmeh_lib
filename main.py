import telebot
from telebot import types
import datetime

# Создаем экземпляр бота
bot = telebot.TeleBot('6128509852:AAHtAYWFyXbeOlKWRTuAn551gP2CTheKw1c')

# Создаем клавиатурный лейаут
keyboard_layout = types.InlineKeyboardMarkup(row_width=2)
button1 = types.InlineKeyboardButton('Режим работы отделов', callback_data='departments_shedule')
button2 = types.InlineKeyboardButton('Читальные залы', callback_data='reading_halls')
button3 = types.InlineKeyboardButton('Контакты', callback_data='contacts')
button4 = types.InlineKeyboardButton('Ничего не интересует', callback_data='nothing_interesting')
keyboard_layout.add(button1, button2, button3, button4)


# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Получаем имя пользователя из объекта message
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    # Отправляем приветственное сообщение с использованием имени пользователя
    bot.send_message(message.chat.id, f"Привет, {first_name} {last_name}! Что тебя интересует?",
                     reply_markup=keyboard_layout)


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
        bot.send_message(call.message.chat.id, '- Директор библиотеки Сессина Н.В. (812) 490-05-86\n'
                                               '- Зам.директора Перепеч С.Б. +7(812)495-76-84\n'
                                               '- Отдел научной литературы  +7(812)495-76-56\n'
                                               '- Отдел учебной литературы в Главном корпусе +7(812)495-76-97\n'
                                               '- Отдел учебной литературы в УЛК +7(812)490-05-39')
    elif text == 'nothing_interesting':
        bot.send_message(call.message.chat.id, 'Хорошо, если что-то захочешь - обращайся :)')


# Запускаем бота
bot.polling(none_stop=True)
