from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

langs = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="πΊπΏ Uzb - π¬π§ Eng"), KeyboardButton(text="π¬π§ Eng - πΊπΏ Uzb")],
        [KeyboardButton(text="πΊπΏ Uzb - π·πΊ Rus"), KeyboardButton(text="π·πΊ Rus - πΊπΏ Uzb")],
        [KeyboardButton(text="π·πΊ Rus - π¬π§ Eng"), KeyboardButton(text="π¬π§ Eng - π·πΊ Rus")],
    ],
    resize_keyboard=True
)

t = ["πΊπΏ Uzb - π¬π§ Eng","πΊπΏ Uzb - π·πΊ Rus","π·πΊ Rus - π¬π§ Eng","π¬π§ Eng - πΊπΏ Uzb","π·πΊ Rus - πΊπΏ Uzb","π¬π§ Eng - π·πΊ Rus"]

voice = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='π Audio tinglash',callback_data='listen')]
    ]
)