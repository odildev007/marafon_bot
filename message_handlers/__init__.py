from aiogram import Router
from . import users
from . import admins
from . import any

router = Router()

router.include_routers(
    any.router,
    admins.router,
    users.router,
)