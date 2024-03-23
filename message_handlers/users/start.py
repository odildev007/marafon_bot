from aiogram.types import Message
import keyboards

async def user_start_message_answer(message: Message):
    await message.answer("Asosiy menyudasiz!", reply_markup=keyboards.user_menu.as_markup())