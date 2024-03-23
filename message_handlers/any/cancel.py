from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import config
import keyboards

async def cancel_answer(message: Message, state: FSMContext):
    if await state.get_state(): await state.clear()
    if message.from_user.id in config.ADMINS:
        await message.answer("Asosiy menyuasiz!", reply_markup=keyboards.admin_menu.as_markup())
    else:
        await message.answer("Asosiy menyudasiz!", reply_markup=keyboards.user_menu.as_markup())
