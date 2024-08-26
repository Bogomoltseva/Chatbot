
import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
from keyboards import kb1, kb2
from random_fox import fox
from random import randint




API_TOKEN = config.token


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f'Привет', reply_markup=kb1)

@dp.message(Command("info"))
async def command_info(message: types.Message):
    await message.answer("Меня зовут Бот, и я не знаю, что я тут делаю и зачем.")

@dp.message(Command("location"))
async def command_loc(message: types.Message):
    await message.answer("Я нахожусь в атомном городе Республики Беларусь")

@dp.message(Command('fox'))
@dp.message(Command('лиса'))
@dp.message(F.text.lower() == 'покажи лису')
async def command_fox(message: types.Message):
    name = message.chat.first_name
    img_fox=fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)

@dp.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f'{number}')


@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' == msg_user:
        await message.answer(f'Привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока, {name}')
    elif 'ты кто' == msg_user:
        await message.answer(f'Я бот, {name}')
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри, что у меня есть, {name}',reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')

# Запуск бота
async def main():
      await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())