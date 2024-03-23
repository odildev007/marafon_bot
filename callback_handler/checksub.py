from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram import Bot
import keyboards
import states
import config
import sqlPrompts

async def not_sub_channel(callback: CallbackQuery, bot: Bot, state: FSMContext):
    checkSub = await bot.get_chat_member(config.channel_id, callback.from_user.id)
    checkSub = checkSub.status
    if checkSub in ["member", "creator", "adminstrator"]:
            await callback.answer("✅ Obunangiz tasdiqlandi!", show_alert=True)
            await callback.message.delete()

            if sqlPrompts.get_user(callback.from_user.id):
                sqlPrompts.change_user_status(callback.from_user.id, "active")
                await callback.message.answer("Asosiy menyudasiz!", reply_markup=keyboards.user_menu.as_markup())
            else:
                await callback.message.answer("Ism-familyangizni kiriting.", reply_markup=ReplyKeyboardRemove())
                await state.set_state(states.GetUserName.name)
    else: await callback.answer("❗ Siz hali kanalga obuna bo'lmagansiz!", show_alert=True)
