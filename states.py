from aiogram.fsm.state import StatesGroup, State

class GetUserName(StatesGroup):
    name = State()

class changePost(StatesGroup):
    menu_name = State()
    caption = State()
    img = State()
    verifly = State()
class SendMessage(StatesGroup):
    message = State()

class WinnersMessage(StatesGroup):
    type = State()
    message = State()