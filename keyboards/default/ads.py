from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('📝 Xabar Yuborish'),
        ],
        [
            KeyboardButton('👤 Foydalanuvchilar'),
            KeyboardButton('👮🏼‍♂️ Adminlar'),
        ],
        [
            KeyboardButton('📊 Statistika')
        ],
        [
            KeyboardButton('🔙 Chiqish')
        ]

    ],
    resize_keyboard=True
)