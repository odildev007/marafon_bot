from aiogram import Router, F
from aiogram.filters import and_f, CommandStart
from . import start
from . import cancel
from . import reyting
from . import groups
import filters
import states

router = Router()

router.message.register(reyting.get_reyitng_answer, and_f(F.chat.type == "supergroup", F.text == "Reytingni ko'rish"))
router.message.register(groups.group_message_answer, F.chat.type == "supergroup")
router.message.register(start.referal, and_f(CommandStart(), filters.IsReferal()))
router.message.register(start.user_sub_channel_message_answer, filters.CheckSubChannel())
router.message.register(start.user_name_naswer, states.GetUserName.name)
router.message.register(start.not_found_user, filters.CheckUser())
router.message.register(cancel.cancel_answer, F.text == "🚫 Bekor qilish")
router.message.register(reyting.get_reyitng_answer, and_f(F.chat.type == "private", F.text == "Reytingni ko'rish"))
