from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import config
import sqlPrompts

admin_menu = ReplyKeyboardBuilder()
for i in ("Hammaga xabar yuborish", "G'oliblarga xabar yuborish", "Postlarni tahrirlash", "Reytingni ko'rish", "Hisobotlarni olish"):
    admin_menu.button(text=i)
admin_menu.adjust(2, 1, 1)

user_menu = ReplyKeyboardBuilder()
for i in ("Mening taklif havolam", "Sovg'alar", "Ballarim", "Reytingni ko'rish"):
    user_menu.button(text=i)
user_menu.adjust(1, 2, 1)

cancel_keyboard = ReplyKeyboardBuilder()
cancel_keyboard.button(text="🚫 Bekor qilish")

sub_channel_menu = InlineKeyboardBuilder()
sub_channel_menu.button(text="Kanalga obuna bo'lish", url=config.channel_url)
sub_channel_menu.button(text="Guruhga obuna bo'lish", url=config.group_url)
sub_channel_menu.button(text="✅ Tekshirish", callback_data="checksub")
sub_channel_menu.adjust(1)

post_menu_keyboards = ReplyKeyboardBuilder()
for i in sqlPrompts.get_all_posts():
    post_menu_keyboards.button(text=i["menu_name"])
post_menu_keyboards.attach(cancel_keyboard)

post_not_img_keyboard = ReplyKeyboardBuilder()
post_not_img_keyboard.button(text="Rasm yo'q")
post_not_img_keyboard.attach(cancel_keyboard)
post_not_img_keyboard.adjust(1)

post_save_keyboards = ReplyKeyboardBuilder()
post_save_keyboards.button(text="✅ Saqlash")
post_save_keyboards.button(text="🚫 Bekor qilish")

send_winners_keyboard = ReplyKeyboardBuilder()
for i in ("1-o'rin", "2-o'rin", "3-o'rin", "4-o'rin", "5-o'rin", "boshqalar"):
    send_winners_keyboard.button(text=i)
send_winners_keyboard.attach(cancel_keyboard)
send_winners_keyboard.adjust(2)
