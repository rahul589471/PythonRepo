import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
from pygame import mixer
import wikipedia
import smtplib
from googletrans import Translator
import pywhatkit as kit


from Exercises import file_handling
from Exercises import snake_water_gun

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio);
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if 0 < hour <= 12:
        speak("Good morning Rahul")
    elif 12 <= hour < 18:
        speak("Good afternoon Rahul")
    else:
        speak("Good Evening Rahul")

    speak("My name is Rahul Robot. \n"
          "How may I help you today !")


def takeCommand():
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        # r.energy_threshold = 50
        # r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("Sorry, say it again..")
        return "none"

    return query


def TranslationHinditoEnglish(text):
    line = str(text)
    translate = Translator()
    result = translate.translate(line,'English')
    data = result.text
    print(f"You :{data}")
    return data


def MicExecution():
    query1 = takeCommand()
    data = TranslationHinditoEnglish(query1)
    print("data is ", data)
    return data


if __name__ == '__main__':
    wishme()
while True:
    query = MicExecution()
    query =query.lower()
    print("query is" ,query)
    # Logic for executing tasks

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    if "youtube" in query:
        speak("Sure sir. Which video?")
        video_name =takeCommand()
        kit.playonyt(video_name)
        #webbrowser.get(chrome_path).open("youtube.com")

    elif "whatsapp" in query:
        try:
            phone_no ='+919650477889'
            speak("What message , sir")
            message =takeCommand()
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute + 1
            kit.sendwhatmsg(phone_no, message, hour,minute)
            speak("Whatsapp message sent")
        except Exception as e:
            print("Exception")
            print(e)

    elif "open chrome" in query:
        webbrowser.get(chrome_path).open("google.com")

    elif "close chrome" in query:
        os.system("taskkill /im chrome.exe /f")

    elif "gmail" in query:
        webbrowser.get(chrome_path).open("gmail.com")

    elif "stack overflow" in query:
        webbrowser.get(chrome_path).open("stackoverflow.com")

    elif "athar" in query:
        speak("Atharv is a sweet boy")

    elif "play music" in query:
        mixer.init()
        print("music started playing....")
        try:
            if __name__ == '__main__':
                mixer.music.load('Exercises//01. Bhool Bhulaiyaa.mp3')
                print("music ended playing....")
                mixer.music.set_volume(5.0)

                # Play the music
                mixer.music.play()
        except:
            print("Error")

    elif "stop the music" in query:
        mixer.music.stop()

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The Time is {strTime}\n")

    elif "pdf" in query:
        speak("Please provide me any valid PDF sir")
        takeCommand()
        speak("Sure sir. Here is your pdf content")
        file_handling.pdfread_sample()

    elif "write to text file" in query:
        speak("Sure sir. Please tell me what to write in file.")
        file_content_to_write= takeCommand()
        file_handling.txtfilewrite_sample(file_content_to_write)
        speak("Your content is written to txt file , Sir")

    elif "read the text file" in query:
        speak("Sure sir.")
        speak(file_handling.txtfileread_sample())


    elif "play a game" in query:
        speak("Sure Sir. You can play now")
        game_return = snake_water_gun.play_game()

        if game_return == 0:
            speak("Thanks for playing sir")

    elif "wikipedia" in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipidea")
            print(results)
            speak(results)
        except Exception as e:
            print("Say again correctly")

    elif "thank" in query:
        speak("Welcome sir")

    elif "how are you" in query:
        speak("I am good. How are you sir?")

    elif "open visual studio code" in query:
        code_path = "C:\\Users\\Rahul\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
        os.startfile(code_path)

    elif "open sql" in query:
        code_path = "C:\\Users\\Rahul\\Downloads\\sqldeveloper\\sqldeveloper.exe"
        os.startfile(code_path)

    elif "send an email" in query:
        try:
            speak("What should I say")
            email_content = takeCommand()
            email_receiver = "rahul.mittal116@gmail.com"
            email_sender = "rahul.mittal116@gmail.com"
            email_subject = "Email from Rahul Robot"
            email_password = 'rxrdtvwfeppyqlbh'

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_receiver, email_content)
            server.close()
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry sir, I am not able to send email")

    elif "bye" in query:
        speak("Have a nice day Sir")
        break
