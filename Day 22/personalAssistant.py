import smtplib

import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

def sendEmail(to, sub, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('practicewitharjya@gmail.com', 'Java@1234')
    server.sendmail('practicewitharjya@gmail.com', to, f"Subject: {sub}\n\n{msg}")
    server.close()

def takeCommand():
    # This function will take input from user by using Microphone and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am started listening to You!!!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Please say that again")
        return "None"
    return query

if __name__ == '__main__':
    greetings()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = "D:\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif 'open paint' in query:
            print("Opening Paint")
            speak("Opening Paint, Please wait")
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint"
            os.startfile(codePath)

        elif 'mail' in query:
            try:
                print("What should be the mail content?")
                speak("What should be the mail content?")
                content = takeCommand()
                subject = "Python By Codehub Academy"
                to = "arjya.net@gmail.com"
                sendEmail(to, subject, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")