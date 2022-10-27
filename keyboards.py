from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

langs = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 Uzb - 🇬🇧 Eng"), KeyboardButton(text="🇬🇧 Eng - 🇺🇿 Uzb")],
        [KeyboardButton(text="🇺🇿 Uzb - 🇷🇺 Rus"), KeyboardButton(text="🇷🇺 Rus - 🇺🇿 Uzb")],
        [KeyboardButton(text="🇷🇺 Rus - 🇬🇧 Eng"), KeyboardButton(text="🇬🇧 Eng - 🇷🇺 Rus")],
    ],
    resize_keyboard=True
)

t = ["🇺🇿 Uzb - 🇬🇧 Eng","🇺🇿 Uzb - 🇷🇺 Rus","🇷🇺 Rus - 🇬🇧 Eng","🇬🇧 Eng - 🇺🇿 Uzb","🇷🇺 Rus - 🇺🇿 Uzb","🇬🇧 Eng - 🇷🇺 Rus"]

voice = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🎙 Audio tinglash',callback_data='listen')]
    ]
)