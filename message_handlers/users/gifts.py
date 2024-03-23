from aiogram.types import Message
import sqlPrompts


async def gifts_answer(message: Message):
    post = sqlPrompts.get_post("Sovg'alar")
    if post["img"]:
        await message.answer_photo(post["img"], caption=post["caption"])
    else:
        await message.answer(post["caption"])
