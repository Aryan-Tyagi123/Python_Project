import pyttsx3   # for speak
import datetime  # for datetime
import speech_recognition as sr    # for microphone
import wikipedia   # using wikipedia
import webbrowser  # for webbrowser
import os  # for music
import subprocess  # for camera
import smtplib #for send email to gmail by arcy


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am Arcy")
    speak("Can you tell me what can I do for you")
        
def takeCommand():
    #It takes microphone imput from the usesr and returns string output   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        
        print("say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.edu.in', 587)
    server.ehlo()
    server.starttls()
    server.login('mca22.aryan.tyagi@sunstone.edu.in', 'aryantyagi123')
    server.sendmail('mca22.aryan.tyagi@sunstone.edu.in',to, content)
    server.close()
    
    
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()   
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open google_chrome' in query:
            webbrowser.open("google_chrome")
            
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
            
        elif 'play music' in query:
             music_dir = 'D:\\Non Critical\\songs\\favorite Songs2' #copy songs folders paths
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")
            
        elif 'open code' in query:
            codepath = "C:\\Users\\Aryan Tyagi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   #copy the path of vs code
            os.startfile(codepath)
            
        elif 'open camera' in query:
            subprocess.run("start microsoft.windows.camera:",shell = True)
            
        elif  'open notepad' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad" #copy the path of notepad
            os.startfile(codepath)
            
        elif 'email to Aryan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mca22.aryan.tyagi@sunstone.edu.in"
                sendEmail(to,content)
                speak("Email has been send!")
                
            except Exception as e:
                print(e)
                speak("sorry my friend aryan. I am not able to send this email")
                
                