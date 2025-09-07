import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"IT":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=7ae1fd1b56c6400496f046efa967eb9e",
                "business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=7ae1fd1b56c6400496f046efa967eb9e",
                "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=7ae1fd1b56c6400496f046efa967eb9e",
                "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=7ae1fd1b56c6400496f046efa967eb9e",
                "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=7ae1fd1b56c6400496f046efa967eb9e"}
    
    content = None
    url = None
    speak("which field news do you want ,[IT] , [business] , [sports] , [science] , [technology]")
    field = input("type field news that you want :")
    for Key , value in api_dict.items():
        if Key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
            if url is True:
                print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news")

    arts = news["articles"]
    for articles in arts :
        articles = articles["title"]
        print(articles)
        speak(articles)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cout] and [press 2 to stop]")
        if str(a) == 1:
            pass
        elif str(a) == 2:
            break

        speak("Thats all")


                                