TOKEN = '5157181393:AAGmANvJcoVkZOfztT-Zag9FJJJRBeFnjW0'

from gtts import gTTS

def text_voice(text,lang):
    myobj = gTTS(text=text,lang=lang,slow=False)
    myobj.save('audios/audio.mp3')