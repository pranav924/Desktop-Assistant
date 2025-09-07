import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import keyboard
import random
import webbrowser
import psutil
from plyer import notification
from pygame import mixer

for i in range(3):
    a = input("Enter password to open Assistant :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLS SPEAK [HELLO] TO LOAD UP")
        break
    elif (i==2 and a!=pw):
        exit()
    elif (a!=pw):
        print("Try Again")

  
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
        
        audio = r.listen(source,0,2)

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "hello" in query:
            from GreetMe import greetMe
            greetMe()
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir , you can call me anytime")
                    break
                   
     ########### ASSISTANT: THE Trilogy 2.0 #########
        
                elif "change password" in query:
                   speak("what' the new password")
                   new_pw = input("Enter the new password\n")
                   new_password = open("password.txt","w")
                   new_password.write(new_pw)
                   new_password.close()
                   speak("Done sir")
                   speak(f"your new password is{new_pw}")


                elif "schedule my day" in query:
                    tasks = [] #Empty list
                    speak("Do you want to clear old tasks (Plz speak YES or  no)")
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the tasks :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the tasks :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                    elif "show my schedule" in query:
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.musics.play
                        notification.notify(
                            title = "my schedule :-",
                            meassge = content,
                            timeout = 15
                        )


      ################################################

                elif "hello" in query:
                    speak("hello sir , how are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("perfect , sir")
                elif "thank you" in query:
                    speak("you are welcome ,sir")

                elif "tired" in query:
                    speak("playing your favorite songs,sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/results?search_query=arijit+singh+songs")
                                   
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down , sir")
                    volumedown() 
                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)



                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()   

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("Assistant","")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
 
                elif "temperature" in query:
                    search = "temperature in solapur"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")


                elif "weather" in query:
                    search = "weather in solapur"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:-10 and 10 and 10")
                    speak("set the time")
                    a = input("please tell the time :-")
                    alarm(a)
                    speak("Done,sir")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir , the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Assistant","")
                    speak("you told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("you told me" + remember.read())

                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer?  (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
                    

