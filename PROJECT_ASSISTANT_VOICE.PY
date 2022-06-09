from email.mime import audio
import imp
from logging import exception
from threading import main_thread
from time import struct_time
from tkinter.tix import MAIN
from unittest import result
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[0].id)
# select voice from pc 0 for men voice ,1 for female voice
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)  # used to get hour for wish
    if hour >= 0 and hour <= 12:
        speak("Good morning nikhil sir")
    elif hour >= 12 and hour < 18:
        speak("Good evening nikhil sir")
    else:
        speak("Good afternoon nikhil sir")

    speak("i am lazer sir , plese tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except exception as e:
      #  print(e)
        print("say again")
        return "none"
    return query


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()

        if 'wilipedia' in query:
            speak('searching in wikipedia')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(" According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open email' in query:
            webbrowser.open("gmail.com")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
        elif 'play music' in query:
            webbrowser.open(
                "https://www.youtube.com/watch?v=bUDIm1SstAE&list=PLldRXoeaXPNm2wL1iy2fBMc55c1T8ZLhp&index=1&ab_channel=ZeeMusicCompany")
        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strTime}")
        elif 'open vscode ' in query:
            codepath = "C:\\Users\\Nikhil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open telegram ' in query:
            telepath = "C:\\Users\\Nikhil\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telepath)
        elif 'exit' in query:
            exit(0)
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'how are you ' in query:
            speak("i am fine how are you sir")
        else:
            speak("oops ,not able to understand sir can you speak it again ")
