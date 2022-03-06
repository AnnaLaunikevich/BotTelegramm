# импорт
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton
# создаем кнопки районов
button_1 = KeyboardButton('Партизанский район')
button_2 = KeyboardButton('Фрунзенский район')
button_3 = KeyboardButton('Советский район')
# уменьшаем кнопки и удаляем после нажатия
markup1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup1.add(button_1).add(button_2).add(button_3)


# создание кнопок с ссылками на сайты школ Партизанского района
button_4 = InlineKeyboardButton("Сайт школы № 22", url='http://sch22.minsk.edu.by')
markup2 = InlineKeyboardMarkup()
markup2.add(button_4)
button_5 = InlineKeyboardButton("Сайт школы № 69", url='http://sch69.minsk.edu.by')
markup3 = InlineKeyboardMarkup()
markup3.add(button_5)
button_6 = InlineKeyboardButton("Сайт школы № 86", url='http://sch86.minsk.edu.by')
markup4 = InlineKeyboardMarkup()
markup4.add(button_6)
button_7 = InlineKeyboardButton("Сайт школы № 133", url='http://sch133.minsk.edu.by')
markup5 = InlineKeyboardMarkup()
markup5.add(button_7)
button_8 = InlineKeyboardButton("Сайт школы № 108", url='http://sch108.minsk.edu.by')
markup6 = InlineKeyboardMarkup()
markup6.add(button_8)
button_9 = InlineKeyboardButton("Сайт гимназии № 5", url='http://gymn5.minsk.edu.by')
markup7 = InlineKeyboardMarkup()
markup7.add(button_9)


# создание кнопок с ссылками на сайты школ Фрунзенского района
button_10 = InlineKeyboardButton("Сайт школы № 81", url='http://sch81.minsk.edu.by')
markup8 = InlineKeyboardMarkup()
markup8.add(button_10)
button_11 = InlineKeyboardButton("Сайт школы № 125", url='http://sch125.minsk.edu.by')
markup9 = InlineKeyboardMarkup()
markup9.add(button_11)
button_12 = InlineKeyboardButton("Сайт школы № 128", url='http://sch128.minsk.edu.by')
markup10 = InlineKeyboardMarkup()
markup10.add(button_12)
button_13 = InlineKeyboardButton("Сайт школы № 151", url='http://sch151.minsk.edu.by')
markup11 = InlineKeyboardMarkup()
markup11.add(button_13)
button_14 = InlineKeyboardButton("Сайт школы № 159", url='http://sch159.minsk.edu.by')
markup12 = InlineKeyboardMarkup()
markup12.add(button_14)
button_15 = InlineKeyboardButton("Сайт гимназии № 4", url='http://gymn4.minsk.edu.by')
markup13 = InlineKeyboardMarkup()
markup13.add(button_15)


# создание кнопок с ссылками на сайты школ Советского района
button_16 = InlineKeyboardButton("Сайт школы № 34", url='http://sch34.minsk.edu.by')
markup14 = InlineKeyboardMarkup()
markup14.add(button_16)
button_17 = InlineKeyboardButton("Сайт школы № 66", url='http://sch66.minsk.edu.by')
markup15 = InlineKeyboardMarkup()
markup15.add(button_17)
button_18 = InlineKeyboardButton("Сайт школы № 78", url='http://sch78.minsk.edu.by')
markup16 = InlineKeyboardMarkup()
markup16.add(button_18)
button_19 = InlineKeyboardButton("Сайт школы № 122", url='http://sch122.minsk.edu.by')
markup17 = InlineKeyboardMarkup()
markup17.add(button_19)
button_20 = InlineKeyboardButton("Сайт школы № 148", url='http://sch148.minsk.edu.by')
markup18 = InlineKeyboardMarkup()
markup18.add(button_20)
button_21 = InlineKeyboardButton("Сайт гимназии № 8", url='http://gymn8.minsk.edu.by')
markup19 = InlineKeyboardMarkup()
markup19.add(button_21)

# создание кнопок с названиями школ районов
button_part1 = KeyboardButton('Средняя школа № 22')
button_part2 = KeyboardButton('Средняя школа № 69')
button_part3 = KeyboardButton('Средняя школа № 86')
button_part4 = KeyboardButton('Средняя школа № 133')
button_part5 = KeyboardButton('Средняя школа № 108')
button_part6 = KeyboardButton('Гимназия № 5')
markup20 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup20.add(button_part1, button_part2, button_part3).add(button_part4, button_part5, button_part6)
button_fr1 = KeyboardButton('Средняя школа № 81')
button_fr2 = KeyboardButton('Средняя школа № 125')
button_fr3 = KeyboardButton('Средняя школа № 128')
button_fr4 = KeyboardButton('Средняя школа № 151')
button_fr5 = KeyboardButton('Средняя школа № 159')
button_fr6 = KeyboardButton('Гимназия № 4')
markup21 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup21.add(button_fr1, button_fr2, button_fr3).add(button_fr4, button_fr5, button_fr6)
button_s1 = KeyboardButton('Средняя школа № 34')
button_s2 = KeyboardButton('Средняя школа № 66')
button_s3 = KeyboardButton('Средняя школа № 78')
button_s4 = KeyboardButton('Средняя школа № 122')
button_s5 = KeyboardButton('Средняя школа № 148')
button_s6 = KeyboardButton('Гимназия № 8')
markup22 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup22.add(button_s1, button_s2, button_s3).add(button_s4, button_s5, button_s6)


