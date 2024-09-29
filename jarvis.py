import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
#import random 
from requests import get
import wikipedia as wp
import webbrowser
from googlesearch import search
import pywhatkit as w

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#To convirt voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening you...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<20:
        speak("Good Evening")
    else:
        speak("Good Night")
    
    speak("Sir I am Jack How can I help you sir")

if __name__ == "__main__":
    #speak("Hi Soubhagya This is advance jarvice How can I help you")
    wish()
    if 1:

        query = takecommand().lower()

        #logic buliding for nodepad

        if "open nodepad" in query:
            # npath = "C:\\WINDOWS\\system32\\nodepad.exe"
            # os.startfile(npath)
            os.system("start notepad")
        
        elif "open powershell" in query:
            # cpath = "C:\\WINDOWS\\system32\\cmd.exe"
            # os.startfile(cpath)
            os.system("start powershell")
        
        elif "fuck you" in query:
            speak("Buro... ki... maa... ki... chud...")

        elif "wikipedia" in query:
            #speak("Searching wikipedia...")
            print("Searching wikipedia...")
            query = takecommand().lower()
            query = query.replace("wikipedia",query)
            #results = wp.search(query,results = 5)
            results=wp.summary(query,sentences=2)
            #speak("wikipedia said that")
            speak(results)
            print(results)
        
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        
        elif "open google" in query:
            #speak("Searching wikipedia...")
            print("Searching google...")
            que = takecommand().lower()
            #query = query.replace("wikipedia",query)
            #results = webbrowser.open(que)
            results = w.search(que)
            #results=wp.summary(query,sentences=2)
            #speak("wikipedia said that")
            speak(results)
            print(results)

        elif "google" in query:
            que = takecommand().lower()
 
            for j in search(que):
                print(j)

        elif "send message" in query:
            w.sendwhatmsg("+917363928885","hi I am Jack your asistant",17,32)

        elif "play youtube" in query:
            que = takecommand().lower()
            w.playonyt(que)
