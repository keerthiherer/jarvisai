import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import requests
import time
import json
import numbers
from bs4 import BeautifulSoup
import wolframalpha
import pywhatkit
try:
    app = wolframalpha.Client("5VWLT4-3GUJKPAVRK")
except Exception:
    print("error occured")



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes Listening Sir...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("owner said:" + query)


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    query = query.lower()
    return query



def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        print(headline.text)
        url = 'https://inshorts.com/en/read'
        response = requests.get(url)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('GMAIL ADDRESS', 'PASSWORD')
    server.sendmail('GMAIL ADDRESS', to, content)
    server.close()



def TaskExecution():
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'read news' in query:
            speak("yes sir")
            print_headlines()
           # print_headlines(response.text)
           # speak(response.text)
           

        elif 'weather report' in query:
            speak("yes sir searching today whether report")
            print("which city should i search for")
            speak('which city should i search for')
            city = takeCommand().lower()
            print('Displaying Weather report for: ' + city)
            url = 'https://wttr.in/{}'.format(city)
            res = requests.get(url)
            print(res.text)
            speak("here is the weather report")

        elif 'open gmail' in query:
            speak("yes sir")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'play on youtube ' in query:
            song = query.replace('play on youtube ', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open google chrome' in query:
            speak("yes sir opening chrome webbrowser")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

      
        elif 'ok bye' in query:
            speak("yes sir")
            speak("see you later sir you can call me any time ")
            print("see you later sir you can call me any time")
            break

    
        elif 'temperature' in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                speak("error")


        elif 'mathematics' in query:
            try:
                speak("what shall i perform sir")
                maths = takeCommand().lower()
                res = app.query(maths)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                speak("error occured")
                print("error occured")

        elif 'science' in query:
            try:
                speak("what sahll i perform sir")
                sci = takeCommand().lower()
                res = app.query(sci)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("error occured")
                speak("error occured")

        elif 'jarvis can you send email' in query:
            speak("yeah sure sir")


        elif 'open calendar' in query:
            speak("yes sir opening online calender")
            webbrowser.open("https://calendar.online/")

        elif 'open Translater' in query:
            speak("yes sir opening translater")
            webbrowser.open("https://translate.google.co.in/?sl=hi&tl=en&op=translate")


        elif 'open youtube' in query:
            speak("yes sir ")
            webbrowser.open("https://www.youtube.com")

        elif 'introduce yourself' in query:
            speak("yes sir. I am your personal assistant")
            speak("i am small assistance for this computer. working using loop concept with limited functions. created by G.KEERTHI BALAN.  ")
            speak("I am running through the python programming language.")
            speak("And i am more advance than alexa, siri and other assistance.")

        elif 'open google' in query:
            speak("opening google sir")
            speak("what shall i search for sir")
            webbrowser.open("https://www.google.com/search?q=" + takeCommand().lower())

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("www.stackoverflow.com")

        elif 'open my website' in query:
            speak("yes sir")
            webbrowser.open("https://keerthibalan.wordpress.com/")

        elif 'open my favourite website' in query:
            speak("sure sir")
            webbrowser.open("https://astralprojectionbykeerthibalan.wordpress.com")

        elif 'play music' in query:
            speak("wait for some times sir... because i am choosing better song for you")
            song = query.replace('play music ', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is {strTime}")

        elif 'open brave' in query:
            speak("yes sir")
            speak("opening brave")
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)

        elif 'how are you jarvis' in query:
            speak(" Sir I Am fine sir ")



        elif 'open map' in query:
            speak("yes sir opening google map")
            speak("which place shall i search for sir.")
            webbrowser.open("https://www.google.com/maps/place/" + takeCommand().lower())


        elif 'say some funny joke' in query:
            speak("yes sir")
            My_joke = pyjokes.get_joke(language="en", category="all")
            print(My_joke)
            speak(My_joke)


        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")


        elif 'open cmd' in query:
            speak("opening command promt")
            os.system('start cmd')

        elif 'open notepad' in query:
            speak("opening notepad sir")
            os.system('start notepad')

    
        elif 'convert speech to text' in query:
            speak("yes sir i am ready. type y when you are ready")
            hello = input("y or n:")
            if 'y' in hello:
                s = takeCommand().lower()
                print(s)
                speak(s)
            else:
                continue

        elif 'open my projects' in query:
            speak("opening your project")
            codePath = "C:\\main\\main.py"
            os.startfile(codePath)

       

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                speak("sir give me receiver address sir")
                to = "stukeerthibalang6122@kvschennairegion.in"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email because there is no internet connection.")
        elif "ok" in query:
           try:
             query = query.replace("okay", "")
             res = app.query(query)
             print(next(res.results).text)
             speak(next(res.results).text)
           except:
                print("error occured")
                speak("error occured, so searching google")
                query = query.replace("okay","")
                webbrowser.open("https://www.google.com/search?q=" +query )

if __name__ == "__main__":
    while True:
        ww = input("Enter the permission yes or no:")
        permission = ww
        if "yes" in permission:
            TaskExecution()
        elif "no" in permission:
            print("okay sir i am sleeping you can call me later")
            exit(TaskExecution())
            
