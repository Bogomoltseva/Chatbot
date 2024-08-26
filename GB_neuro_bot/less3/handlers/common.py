from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.keyboards.keyboards import kb1, kb2
from less3.utils.random_fox import fox
from random import randint


router = Router()


@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f'Привет', reply_markup=kb1)

@router.message(Command("info"))
async def command_info(message: types.Message):
    await message.answer("Меня зовут Бот. Я тут новичок.")

@router.message(Command("location"))
async def command_loc(message: types.Message):
    await message.answer("Я нахожусь в атомном городе Республики Беларусь")


@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def command_fox(message: types.Message):
    name = message.chat.first_name
    img_fox=fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)

@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f'{number}')


@router.message(F.text)
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
        await message.answer(f'Попробуй еще раз, {name}')