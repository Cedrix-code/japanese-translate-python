from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from gtts import lang
import os

print(lang.tts_langs())

# Capturing the voice command
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said: {query}\n")
    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query

# Setting the destination language to Japanese
to_lang = 'ja'
# Defining the query variable
query = takecommand()
# Translating from English to Japanese
translator = Translator()
text_to_translate = translator.translate(query, dest=to_lang)

# Getting the translated text
text = text_to_translate.text

# Using Google-Text-to-Speech to speak the translated text in Japanese
speak = gTTS(text=text, lang=to_lang, slow=False)

# Printing the output
print(f"Translated to Arabic: {text}")
# Saving the translated speech in a file
speak.save("captured_voice.mp3")

# Playing the translated speech
playsound('captured_voice.mp3')

# Removing the temporary file
os.remove('captured_voice.mp3')

