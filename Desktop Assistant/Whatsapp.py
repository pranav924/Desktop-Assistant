import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime

 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    a = int(input('''person 1-1
              person 2-2'''))
    if a == 1:
        speak("what the message")
        message = str(input("enter the message- "))
        pywhatkit.sendwhatmsg("+918380914858",message,time_hour=strTime,time_min=update)
    elif a==2:
        speak("what the message")
        message = str(input("enter the message- "))
        pywhatkit.sendwhatmsg("+918975733764",message,time_hour=strTime,time_min=update)
        
        pass