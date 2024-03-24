from aiogram.types import Message
import sqlPrompts


async def my_ref_link_answer(message: Message):
    post = sqlPrompts.get_post("Mening taklif havolam")
    post["caption"] = post["caption"].replace("Link uchun joy", f"https://t.me/geometriyamarafonbot?start={message.from_user.id}" )
    if post["img"]:
        await message.answer_photo(post["img"], caption=post["caption"])
    else:
        await message.answer(post["caption"])
