import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3

engine=pyttsx3.init()

def speak(text):
    print(f"{text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour=datetime.datetime.now().hour
    if hour<12:
        speak("good morning")
    elif 12<=hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis. how can i assist you today?")

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening")
        try:
            audio=r.listen(source,timeout=5)
            command =r.recognize_google(audio).lower()
            return command

        except sr.UnknownValueError:
            speak("sorry, i didn't catch that. could you say it again" )
            return ""
        except sr.RequestError:
            speak('i am having trouble connecting to the internet')
            return ""
        except sr.WaitTimeoutError:
            speak("you didn't say anything")
            return ""

def open_website(command):
    sites={
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "amazon": "https://www.amazon.com",
        "linkedin": "https://www.linkedin.com",
        "myntra" : "https://www.myntra.com"
    }

    for site in sites:
        if site in command:
            webbrowser.open(sites[site])
            speak(f"opening {site}")
            return True
    speak("i didn't find any matching website in your command")
    return False
        
def respond_to_command(command):
    if "time" in command:
        current_time=datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"the current time is {current_time}")
        return True

   
        
    elif "search " in command:
        speak("what should i search for?")
        query=take_command()
        if query:
            webbrowser.open(f"https://google.com/search?q={query}")
            speak(f"searching for {query}")
            return True
        elif "exit" in command or "bye" in command:
            speak('goodbye! have a great day!')
            return False
        else:
            speak("i didn't understand that please try again")
            return True

def your_developer(command):
    if "your developer" in command:
        speak(" i was created by farwa , a second year bca student")
        return True

if __name__=="__main__":
    greet_user()
    while True:
        command=take_command()
        if command: 
            if "exit" in command or "bye" in command:
                speak("goodbye! have a great day")
                break
            elif "open" in command:
                if open_website(command):
                    continue
        
            else:
                handled=respond_to_command(command)
                if not handled:
                    speak("i didn't understand that . please try again")
