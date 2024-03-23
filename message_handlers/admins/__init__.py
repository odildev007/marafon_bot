from aiogram import Router, F
from aiogram.filters import CommandStart, and_f
from . import start
from . import change_post
from . import send
from . import reports
import filters
import states


router = Router()

router.message.register(start.start_message, and_f(filters.IsAdmin(), CommandStart()))
router.message.register(change_post.change_post_answer, and_f(filters.IsAdmin(), F.text == "Postlarni tahrirlash"))
router.message.register(change_post.change_post_menu_name_answer, and_f(filters.IsAdmin(), states.changePost.menu_name))
router.message.register(change_post.change_post_caption_answer, and_f(filters.IsAdmin(), states.changePost.caption))
router.message.register(change_post.change_post_img_answer, and_f(filters.IsAdmin(), states.changePost.img))
router.message.register(change_post.change_post_verify_answer, and_f(filters.IsAdmin(), states.changePost.verifly))
router.message.register(send.all_users_send_message_answer, and_f(filters.IsAdmin(), F.text == "Hammaga xabar yuborish"))
router.message.register(send.all_users_send_message_message_answer, states.SendMessage.message)
router.message.register(send.winners_send_message_type_answer, and_f(filters.IsAdmin(), F.text== "G'oliblarga xabar yuborish"))
router.message.register(send.winners_send_message_answer, states.WinnersMessage.type)
router.message.register(send.winners_send_message_message_answer, states.WinnersMessage.message)
router.message.register(reports.send_reports_answer, and_f(filters.IsAdmin(), F.text == "Hisobotlarni olish"))
router.message.register(reports.get_db, and_f(filters.IsAdmin(), F.text == "data"))