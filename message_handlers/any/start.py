from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Bot
from aiogram.fsm.context import FSMContext
import keyboards
import sqlPrompts
import states
import config

async def user_sub_channel_message_answer(message: Message, state: FSMContext):
    if sqlPrompts.get_user(message.from_user.id):
        sqlPrompts.change_user_status(message.from_user.id, "warm")
        if sqlPrompts.check_user_referal(message.from_user.id, 404) != 3:
            sqlPrompts.change_referal_status(message.from_user.id, "warm")
    
    await message.answer("Kanalga obuna bo'ling.", reply_markup=keyboards.sub_channel_menu.as_markup())

async def user_name_naswer(message: Message, bot: Bot, state: FSMContext):
    if len(message.text.split()) == 2:
        sqlPrompts.add_user(message.from_user.id, message.text)
        reffer_id = sqlPrompts.get_user_reffer_id(message.from_user.id)

        if reffer_id:

            sqlPrompts.change_referal_status(message.from_user.id, "active")
            await bot.send_message(reffer_id['reffer_id'], text="✅ Sizga 1 ball qo'shildi!")
        for i in config.ADMINS:
            await bot.send_message(i, f"<b>YANGI FOYDALANUVCHI:</b>\n\n<b>Ism-familya:</b> {message.text} - {message.from_user.mention_html('Profil')}", parse_mode="HTML")
        if message.from_user.id in config.ADMINS:
            await message.answer(f"{message.text}, siz muvaffaqiyatli royhatdan o'tdingiz!", reply_markup=keyboards.admin_menu.as_markup())
        else:
            await message.answer(f"{message.text}, siz muvaffaqiyatli royhatdan o'tdingiz!", reply_markup=keyboards.user_menu.as_markup())
        await state.clear()
    else:
        await message.answer("Menga ism-familyangizni kiriting.")

async def not_found_user(message: Message, state: FSMContext):
    await message.answer("Ism-familyangizni kiriting.", reply_markup=ReplyKeyboardRemove())
    await state.set_state(states.GetUserName.name)

async def referal(message: Message):
    pass

async def this_block_answer(message: Message):
    await message.answer_sticker("CAACAgIAAxkBAAJEPWXkN7T5M3zuyFBmoRKeWOe6qT5-AAI5DwACdrIpSvr8TNGlMJ1aNAQ")
