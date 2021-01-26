import pyttsx3 as p
import speech_recognition as sr
from YT_audio import music
from selenium_web import infow
from News import *
import randfacts
from jokes import *
from weather import *
import datetime

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return "Good morning"
    elif hour >= 12 and hour < 16:
        return "Good afternoon"
    else:
        return "Good evening"

today = datetime.datetime.now()
r = sr.Recognizer()
speak("Hello sir ,"+wishme() + " I'm your voice Assistance.")
speak("Today is" + today.strftime("%d") + " of " + today.strftime("%B") + " And its currently " +today.strftime("%c"))
speak("Temperature in Mumbai is " + str(temp()) + " degree Celsius " + " and with " + str(des()))
speak("what can i do for you?")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak(" i'm Having a good day sir")
speak("what can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))

    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("Playing {} on youtube ".format(vid))
    speak("searching {} in youtube".format(vid))

    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("Sure sir, Now i will Read News For You.")
    speak("Sure sir, Now i will Read News For You.")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure sir, ")
    x = randfacts.getFact()
    print(x)
    speak("Did you know that, " + x)

elif "jokes" or "joke" in text2:
    speak("Sure sir, Get ready for some chuckles")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
