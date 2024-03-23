from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import states
import utils
import sqlPrompts
import keyboards

async def all_users_send_message_answer(message: Message, state: FSMContext):
    markup = keyboards.cancel_keyboard.as_markup()
    markup.resize_keyboard = True
    await message.answer("Foydalanuvchilarga yubormoqchi bo'lgan xabaringizni kiriting.", reply_markup=markup)
    
    await state.set_state(states.SendMessage.message)

async def all_users_send_message_message_answer(message: Message, state: FSMContext):
    all_users_id = []
    for i in sqlPrompts.get_users():
        if i['status'] == "active":
            all_users_id.append(i["user_id"])
    
    sent = await utils.send_message_to_users(all_users_id, message)
    await message.answer(f"Xabar {sent} ta foydalanuvchiga yetkazildi!", reply_markup=keyboards.admin_menu.as_markup())
    await state.clear()

async def winners_send_message_answer(message: Message, state: FSMContext):
    await state.update_data(type=message.text)
    markup = keyboards.cancel_keyboard.as_markup()
    markup.resize_keyboard = True
    await message.answer("Xabaringizni kiriting.", reply_markup=markup)
    await state.set_state(states.WinnersMessage.message)

async def winners_send_message_type_answer(message: Message, state: FSMContext):
    await message.answer("Tanlang.", reply_markup=keyboards.send_winners_keyboard.as_markup())
    await state.set_state(states.WinnersMessage.type)

async def winners_send_message_message_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    type = data.get("type")    
    
    winners = []
    
    users = []
    for i in sqlPrompts.get_users():
        if i['status'] == "active":
            users.append(i)
    
    for user in users:
            referals = sqlPrompts.get_user_referals(user["user_id"])
            ball = 0
            if referals:
                for referal in referals:
                    if referal['status'] == 'active':
                        ball += 1
            if ball: winners.append((user["user_id"], user['name'], ball))
    winners.sort(key=lambda x: x[2], reverse=True)
    k = 1
    users = []

    if winners:
        if type == "1-o'rin":
            users.append(winners[0][0])
        elif type == "2-o'rin":
            users.append(winners[1][0])
        elif type == "3-o'rin":
            users.append(winners[2][0])
        elif type == "4-o'rin":
            users.append(winners[3][0])
        elif type == "5-o'rin":
            users.append(winners[4][0])
        elif type == "boshqalar":
            for j in winners[5:]:
                users.append(j[0])
                k += 1
                if j[2] < 5:
                    break
    await message.answer("Xabar qabul qilindi!")
    sent = await utils.send_message_to_users(users, message)
    await message.answer(f"Xabar {sent} ta foydalanuvchiga yetkazildi!", reply_markup=keyboards.admin_menu.as_markup())
    await state.clear()