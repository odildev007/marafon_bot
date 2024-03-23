from aiogram.types import Message
import sqlPrompts
from datetime import datetime, timedelta, timezone


async def get_reyitng_answer(messsage: Message):
    users = sqlPrompts.get_users()
    reyting = []
    for user in users:
        if user['status'] == "active":
            referals = sqlPrompts.get_user_referals(user["user_id"])
            ball = 0
            if referals:
                for referal in referals:
                    if referal['status'] == 'active':
                        ball += 1
            if ball: reyting.append((user["user_id"], user['name'], ball))
    reyting.sort(key=lambda x: x[2], reverse=True)
    k = 1

    sana = datetime.now()

    target_timezone = timezone(offset=timedelta(hours=5))

    sana = sana.astimezone(target_timezone)

    sana = sana.strftime("%Y.%m.%d %H:%M:%S")
    text = f"<b>Reyting natijalari</b> 📅 {sana}\n\n"
    if reyting:
        user = sqlPrompts.get_user(messsage.from_user.id)
        userFlag = True
        for j in reyting:
            text += f"{k}. {j[1]} - {j[2]} ball\n"
            if j[0] == messsage.from_user.id: userFlag = False
            k += 1
            if k == 11:
                break
        if userFlag:
            text += "\n\n"
            if messsage.chat.type != "supergroup":
                for j in reyting:
                    if j[0] == messsage.from_user.id:
                        orin = reyting.index(j)
                        text += f"{orin + 1}. {j[1]} - {j[2]} - ball"
                        break
                else:
                    text += "<b>Siz hali ball to'plamadingiz!</b>"

    else: text += "<b>Hali hech kim ball to'plamadi!</b>"

    await messsage.answer(text)