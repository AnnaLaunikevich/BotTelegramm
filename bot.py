# Импортируем необходимые модули библиотеки aiogram и токен бота, а так же инициализируем
# объекты бота и диспетчера
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards import markup1
from keyboards import markup2
from keyboards import markup3
from keyboards import markup4
from keyboards import markup5
from keyboards import markup6
from keyboards import markup7
from keyboards import markup8
from keyboards import markup9
from keyboards import markup10
from keyboards import markup11
from keyboards import markup12
from keyboards import markup13
from keyboards import markup14
from keyboards import markup15
from keyboards import markup16
from keyboards import markup17
from keyboards import markup18
from keyboards import markup19

from keyboards.keyboard import markup20
from keyboards.keyboard import markup21
from keyboards.keyboard import markup22

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
CHANNEL_NAME = 'scoolMinsk_bot'

# начало работы бота
# создаем декоратор

@dp.message_handler(commands=['start', 'help'])
# создаем функцию, которую декорируем
async def start_commands(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в помощник по поиску школы для Вашего ребенка!'
                                                 '\nВыберите интересующий Вас район г. Минска:', reply_markup=markup1)

# выбор школы Партизанского района
@dp.message_handler(content_types=["text"])
async def hand_text(message):
    await bot.send_message(message.from_user.id, message.text.strip())
    if message.text.strip() == 'Партизанский район':
        await bot.send_message(message.chat.id, "В Партизанском районе есть следующие школы: ", reply_markup=markup20)
    elif message.text.strip() == 'Средняя школа № 22':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup2)

    elif message.text.strip() == 'Средняя школа № 69':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup3)

    elif message.text.strip() == 'Средняя школа № 86':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup4)

    elif message.text.strip() == 'Средняя школа № 133':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup5)

    elif message.text.strip() == 'Средняя школа № 108':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup6)

    elif message.text.strip() == 'Гимназия № 5':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup7)

# выбор школы Фрунзенского района
    elif message.text.strip() == 'Фрунзенский район':
        await bot.send_message(message.chat.id, "Во Фрунзенском районе есть следующие школы: ", reply_markup=markup21)
    elif message.text.strip() == 'Средняя школа № 81':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup8)

    elif message.text.strip() == 'Средняя школа № 125':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup9)

    elif message.text.strip() == 'Средняя школа № 128':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup10)

    elif message.text.strip() == 'Средняя школа № 151':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup11)

    elif message.text.strip() == 'Средняя школа № 159':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup12)

    elif message.text.strip() == 'Гимназия № 4':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup13)

# выбор школы Советского района
    elif message.text.strip() == 'Советский район':
        await bot.send_message(message.chat.id, "В Советском районе есть следующие школы: ", reply_markup=markup22)
    elif message.text.strip() == 'Средняя школа № 34':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup14)

    elif message.text.strip() == 'Средняя школа № 66':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup15)

    elif message.text.strip() == 'Средняя школа № 78':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup16)

    elif message.text.strip() == 'Средняя школа № 122':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup17)

    elif message.text.strip() == 'Средняя школа № 148':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup18)

    elif message.text.strip() == 'Гимназия № 8':
        await bot.send_message(message.chat.id, "Нажми на кнопку и перейди на сайт)".format(message.from_user),
                               reply_markup=markup19)



if __name__ == '__main__':
    executor.start_polling(dp)
