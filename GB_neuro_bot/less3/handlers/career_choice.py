from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from less3.keyboards.prof_keyboards import make_row_keyboard
from less3.keyboards.keyboards import kb1


router = Router()


available_jobs = [
    'Программист',
    'Дизайнер',
    'Маркетолог'

]

available_grades = ['Junior', 'Midle', 'Senior']

exit_button = 'Выход'

class ChoiceProfile(StatesGroup):
    job = State()
    grade = State()

@router.message(Command('prof'))
async def command_prof(message: types.Message, state: FSMContext):
    keyboard = make_row_keyboard(available_jobs + [exit_button])
    await message.answer('Выберите профессию', reply_markup=keyboard)
    await state.set_state(ChoiceProfile.job)


@router.message(ChoiceProfile.job, F.text.in_(available_jobs))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text)
    keyboard = make_row_keyboard(available_grades + [exit_button])
    await message.answer('Выберите уровень', reply_markup=keyboard)
    await state.set_state(ChoiceProfile.grade)

@router.message(ChoiceProfile.job, F.text == exit_button)
@router.message(ChoiceProfile.grade, F.text == exit_button)
async def exit_button_pressed(message: types.Message, state: FSMContext):
    await message.answer("Давай заново", reply_markup=kb1)
    await state.clear()

@router.message(ChoiceProfile.job)
async def prof_chosen_incorrect(message: types.Message):
    keyboard = make_row_keyboard(available_jobs + [exit_button])
    await message.answer('Выберите профессию', reply_markup=keyboard)


@router.message(ChoiceProfile.grade, F.text.in_(available_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f"Ваша профессия: {user_data['profession']}\n"
                         f"Ваш уровень: {message.text}",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

@router.message(ChoiceProfile.grade)
async def grade_chosen_incorrect(message: types.Message):
    keyboard = make_row_keyboard(available_grades + [exit_button])
    await message.answer('Выберите уровень', reply_markup=keyboard)

@router.message(F.text == exit_button)
async def exit_button_pressed(message: types.Message, state: FSMContext):
    await message.answer("Давай заново", reply_markup=kb1)
