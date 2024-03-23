from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
import aiogram
import config
import message_handlers
import callback_handler
import asyncio


dp = Dispatcher()

async def main():
    bot = Bot(token=config.TOKEN, parse_mode="HTML")

    dp.include_routers(
        message_handlers.router,
        callback_handler.router        
    )


    await dp.start_polling(bot)

asyncio.run(main())