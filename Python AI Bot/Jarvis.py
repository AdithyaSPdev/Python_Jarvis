import pywhatkit
from decimal import InvalidOperation
from email.mime import audio
from enum import auto
from http.client import LENGTH_REQUIRED
from logging import exception
from time import strftime
from winreg import REG_NO_LAZY_FLUSH
import wikipedia
from multiprocessing.context import set_spawning_popen
import os
import webbrowser
import speech_recognition as sr
from pip import main
import pyttsx3
from datetime import datetime


chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)


# making a good morning peperty
def wish():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir ')
    elif hour>12 and hour<18:
        speak('Good  afternoon sir ')
    else:
        speak('good night sir ')

    speak("I am spectra What can I do for you")

# taking command 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in') 
        print(f"user said this : {query}\n")

    except exception as e:
        print(e)
        print('Try again please')
        return "none"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()





if __name__ == '__main__':
    wish()
while True:
        query=  takeCommand().lower()
    #writting code to follow the command by the jarvis 
        if 'wiki' in query:
            speak('searching wikipedia ')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak('According to me')
            print(results)
            speak(results)
    # to close the jarvis 
        elif 'sleep' in query:
            break;
    # to open something
        elif'open youtube' in query:
            speak('I opened youtube for you sir')
            webbrowser.get(chrome_path).open('youtube.com')
    # to open something
        elif'open google' in query:
            speak('I opened google for you sir')
            webbrowser.get(chrome_path).open('google.com')
            
    # to open something
        elif'open github' in query:
            speak('I opened github for you sir')
            webbrowser.get(chrome_path).open('github.com')
    # to open something
        elif'open codewithharry' in query:
            speak('I opened codewithharry for you sir')
            webbrowser.get(chrome_path).open('codewithharry.com')
    # to play a music and making random module
        elif 'play music' in query:
            music_dir  = 'C:\\Users\\AdithyaSPoojary625\\Desktop\\favourite songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
    # to speak the current time 
        elif 'current time' in query:
            strtime = datetime.now().strftime("%H:%M:%S")
            speak(f'sir the Current time is {strtime}')




#  to open  different apps 
        elif 'open chrome' in query:
            browserPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(browserPath)
        elif 'open code' in query:
            codePath = "C:\\Users\\AdithyaSPoojary625\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

# to calculate
        elif'add numbers' in query:
            a = speak('tell the first number')
            s1 = takeCommand()
            print(s1)
            b = speak('tell the second number')
            s2 = takeCommand()
            print(s2)
            sum = int(s1) + int(s2)
            print(sum)
            speak(sum)
        elif'subtract numbers' in query:
            a = speak('tell the first number')
            s1 = takeCommand()
            print(s1)
            b = speak('tell the second number')
            s2 = takeCommand()
            print(s2)
            sum = int(s1) - int(s2)
            print(sum)
            speak(sum)
        elif'multiply numbers' in query:
            a = speak('tell the first number')
            s1 = takeCommand()
            print(s1)
            b = speak('tell the second number')
            s2 = takeCommand()
            print(s2)
            sum = int(s1) * int(s2)
            print(sum)
            speak(sum)
        elif'divide numbers' in query:

    
            a = speak('tell the first number')
            s1 = takeCommand()
            print(s1)
            b = speak('tell the second number')
            s2 = takeCommand()
            print(s2)
            sum = int(s1) / int(s2)
            print(sum)
            speak(sum)
            
    
# a midule to play videos on youtube
        elif "play video" in query:
            speak('Which video sir')
            yt= takeCommand()
            pywhatkit.playonyt(yt)
 

                  