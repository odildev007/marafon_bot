from aiogram.types import Message
import sqlPrompts


async def my_balls_answer(message: Message):
    user_referals = sqlPrompts.get_user_referals(message.from_user.id)
    ball = 0
    if user_referals:
        for referal in user_referals:
            if referal["status"] == "active":
                ball += 1
        
    if not ball: await message.answer("❗ Siz hali botga hech kimni taklif qilmadingiz!")
    else: await message.answer(f"Siz {ball} ball to'pladingiz!")
