# importing packages
import speech_recognition as srecon
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ecap
import wolframalpha
import json
import requests


print("Executing voice assistant")


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def greetings():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
        
def takeCommand():
    r=srecon.Recognizer()
    with srecon.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Can't comprehend")
            return "None"
        return statement


greetings()             #calling greetings function

#defining main function
if __name__=='__main__':
    
    while True:
        speak("Hey how can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "close" in statement or "exit" in statement or "stop" in statement:
            speak('Good bye, shutting down')
            print('Good bye, shutting down')
            break
            
            
        if 'wikipedia' in statement:
            speak('Searching in Wiki...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia, ")
            print(results)
            speak(results)
            
            
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is running now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement or 'news headlines' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
            
            
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        
        elif "camera" in statement or "take a photo" in statement or "capture picture" in statement:
            ecap.capture(0,False,"image1.jpg")
        
        
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
            
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="PYQWQ5-G9QW98V2J3"
            client = wolframalpha.Client('PYQWQ5-G9QW98V2J3')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        
        elif "weather" in statement:
            api_key="6dec10f6c71c06bbceb03b87fbc9004c"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("name the city")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin is " +
                      str(current_temperature) +
                      "\n Percentage humidity is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else: 
                speak("City not found")
        
        
        elif "shutdown" in statement or "shut pc" in statement:
            speak("Roger, your pc will log off in 10 seconds")
            subprocess.call(["shutdown", "/l"])
        
time.sleep(3)      
        