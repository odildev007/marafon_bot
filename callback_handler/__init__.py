from aiogram import Router, F
from . import checksub

router = Router()

router.callback_query.register(checksub.not_sub_channel, F.data.startswith("checksub"))