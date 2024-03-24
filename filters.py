from aiogram import Bot
from aiogram.types import Message
from aiogram.enums import ChatMemberStatus
from aiogram.filters import Filter

import sqlPrompts
import config

class CheckUser(Filter):
    async def __call__(self, message: Message):
        if sqlPrompts.get_user(message.from_user.id):
            sqlPrompts.change_user_status(message.from_user.id, "active")
        else:
            return True

class IsBlockUser(Filter):
    async def __call__(self, message: Message):
        if sqlPrompts.get_user(message.from_user.id) and sqlPrompts.get_user(message.from_user.id)['status'] == "veryblock":
            return True
        return False

class IsAdmin(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id in config.ADMINS

class IsReferal(Filter):
    async def __call__(self, message: Message, bot: Bot):
        if message.text.startswith("/start") and message.text[7:].isdigit():
            reffer_id = int(message.text[7:])
            condition = sqlPrompts.check_user_referal(message.from_user.id, reffer_id) 
            if reffer_id == message.from_user.id:
                await message.answer("Siz o'zingizga referal bo'la olmaysiz!")
            elif condition == 3:
                try:
                    await bot.send_message(reffer_id, f"Sizga yana bir referal qabul qilindi! U to'liq ro'yhatdan o'tgach sizga ball qo'shiladi!")
                    sqlPrompts.add_referal(message.from_user.id, reffer_id)
                except:
                    await message.answer("Bunday foydalanuvchi botda mavjud emas. Ehtimol u botni bloklagandir!")
                
            elif condition == 2:
                await message.answer("Siz oldin boshqa do'stingizga referal bo'lgansiz! Ikkinchi marta referal bo'la olmaysiz!")
            elif condition == 1:
                await message.answer("Siz oldin bu do'stingizga referal bo'lgansiz!")

class CheckSubChannel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        checkSubChan = await bot.get_chat_member(config.channel_id, message.from_user.id)
        checkSubGru = await bot.get_chat_member(config.group_id, message.from_user.id)
        print(checkSubChan.status, checkSubGru.status)
        checkSubChan, checkSubGru = checkSubChan.status, checkSubGru.status
        
        if not checkSubChan in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER] or not checkSubGru in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER]:
            return True


