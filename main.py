from audioop import alaw2lin
from cgitb import text
from email import message
from aiogram import types,Bot,executor,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
from aiogram.dispatcher import FSMContext
from state import Translate
from keyboards import langs,voice,t
from googletrans import Translator
from config import text_voice
import os


@dp.message_handler(commands=['start'],state='*')
async def do_start(message:types.Message):
    name = message.from_user.first_name
    await message.answer(f'🤗 Assalomu alaykum {name} tarjimon botga xush kelibsiz!')
    await message.answer('Quyidagilardan birini tanlang!',reply_markup=langs)
    await Translate.lang.set()

@dp.message_handler(state=Translate.lang)
async def choose_lang(message:types.Message,state:FSMContext):
    lang = message.text
    if lang in t:
        await state.update_data(
            {'lang':lang}
        )
        await message.answer('Tarjima qilinuvchi matnni kiriting!')
        await Translate.next()
    else:
        await message.answer('Iltimos quyidagilardan birini tanlang 👇 ',reply_markup=langs)

@dp.message_handler(state=Translate.trans)
async def transl(message:types.Message,state:FSMContext):
    word = message.text
    data = await state.get_data()
    lang = data.get('lang')
    translator = Translator()
    if lang == '🇺🇿 Uzb - 🇬🇧 Eng':
        translation = translator.translate(word, dest="en")
        await message.answer(translation.text, reply_markup=voice)
        text_voice(translation.text, lang="en")

    elif lang == "🇬🇧 Eng - 🇺🇿 Uzb":
        translation = translator.translate(word, dest="uz")
        await message.answer(translation.text, reply_markup=voice)
        text_voice(translation.text, lang="tr")

    elif lang == "🇺🇿 Uzb - 🇷🇺 Rus":
        translation = translator.translate(word, dest="ru")
        await message.answer(translation.text, reply_markup=voice)
        text_voice(translation.text, lang="ru")

    elif lang == "🇷🇺 Rus - 🇺🇿 Uzb":
        translation = translator.translate(word, dest="uz")
        await message.answer(translation.text, reply_markup=voice)
        text_voice(translation.text, lang="tr")

    elif lang == '🇷🇺 Rus - 🇬🇧 Eng':
        translation = translator.translate(word,dest='en')
        await message.answer(translation.text,reply=voice)
        text_voice(translation.text, lang="en")

    elif lang == '🇬🇧 Eng - 🇷🇺 Rus':
        translation = translator.translate(word,dest='ru')
        await message.answer(translation.text,reply=voice)
        text_voice(translation.text, lang="ru")

    else:
        await message.answer('Quyidagilardan birini tanlang 👇!',reply_markup=langs)
        await Translate.lang.set()

    
    await Translate.voice.set()

@dp.callback_query_handler(text = 'listen',state=Translate.voice)
async def send_audio(call:types.CallbackQuery):
    await call.message.answer_audio(open("audios/audio.mp3", 'rb'), reply_markup=langs)
    os.remove('audios/audio.mp3')
    await Translate.lang.set()


















if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)