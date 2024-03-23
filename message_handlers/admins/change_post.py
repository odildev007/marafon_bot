from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
import sqlPrompts
import states
import keyboards

async def change_post_answer(message: Message, state: FSMContext):
    for post in sqlPrompts.get_all_posts():
        await message.answer(post["menu_name"])
        if post["caption"]:
            if post["img"]:
                await message.answer_photo(post["img"], caption=post["caption"])
            await message.answer(post["caption"])
        else: await message.answer("Post qo'shilmagan!")
    await message.answer("Qaysi menyu postini tahrirlamoqchisiz?", reply_markup=keyboards.post_menu_keyboards.as_markup())
    await state.set_state(states.changePost.menu_name)
    
async def change_post_menu_name_answer(message: Message, state: FSMContext):
    if sqlPrompts.get_post(message.text):
        await state.update_data(menu_name=message.text)
        await message.answer("Menga post matnini yuboring.", reply_markup=ReplyKeyboardRemove())
        await state.set_state(states.changePost.caption)
    else:
        await message.answer("Menyulardan birini tanlang.", reply_markup=keyboards.post_menu_keyboards.as_markup())

async def change_post_caption_answer(message: Message, state: FSMContext):
    await state.update_data(caption=message.html_text)
    await message.answer("✅ Post matni qabul qilindi!")
    await message.answer("Post rasmini yuboring.", reply_markup=keyboards.post_not_img_keyboard.as_markup())
    await state.set_state(states.changePost.img)

async def change_post_img_answer(message: Message, state: FSMContext):
    if message.photo:
        await state.update_data(img=message.photo[0].file_id)
        await message.answer("✅ Post rasmi qabul qilindi!")
    data = await state.get_data()
    if message.photo: await message.answer_photo(message.photo[0].file_id, caption=data.get("caption"))
    else: await message.answer(data.get("caption"))
    await message.answer("Postni saqlayveraymi?", reply_markup=keyboards.post_save_keyboards.as_markup())
    await state.set_state(states.changePost.verifly)
    
async def change_post_verify_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    sqlPrompts.change_post(data.get("img"), data.get("caption"), data.get("menu_name"))
    await message.answer("✅ Post saqlandi!", reply_markup=keyboards.admin_menu.as_markup())
    await state.clear()
