from aiogram.types import Message
import keyboards

async def start_message(message: Message):
    await message.answer("Asosiy menyudasiz!", reply_markup=keyboards.admin_menu.as_markup())

