# Imports
import os
import playsound

from gtts import gTTS

# Functions
def Speak(text):
    path = f"{os.getcwd()}\\Character\\Speak.mp3"

    tts = gTTS(text = text, lang = "ko")
    
    tts.save(path)

    playsound.playsound(path)
    os.remove(path)