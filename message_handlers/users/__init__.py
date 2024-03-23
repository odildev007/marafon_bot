from aiogram import Router, F
from . import start
from . import my_ref_link
from . import gifts
from . import balls
from aiogram.filters import CommandStart

router = Router()

router.message.register(start.user_start_message_answer, CommandStart())
router.message.register(my_ref_link.my_ref_link_answer, F.text == "Mening taklif havolam")
router.message.register(gifts.gifts_answer, F.text == "Sovg'alar")
router.message.register(balls.my_balls_answer, F.text == "Ballarim")