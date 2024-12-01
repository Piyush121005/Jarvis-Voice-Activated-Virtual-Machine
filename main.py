import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from transformers import pipeline

recognizer = sr.Recognizer()
engine = pyttsx3.init()
API_KEY = "f89d9bfe288f453084e9d92086d4f8fa"
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
    
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split()[1]
        link = musicLibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak(f"I couldn't find the song {song}")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles[:5]:  # Limit to the first 5 headlines
                speak(article["title"])
        else:
            speak("Sorry, I couldn't fetch the news.")
    else:
        # Let Hugging Face handle the request
        response = generator(c, max_length=50, num_return_sequences=1, truncation=True)
        reply = response[0]["generated_text"]
        speak(reply)
    



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:

        # Listen for the wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("Listening....")
        try:
            with sr.Microphone() as source:
                print("Recognizing..")
                audio = r.listen(source,timeout = 2,phrase_time_limit=1)
                word = r.recognize_google(audio)
                if(word.lower()=="hello"):
                    speak("ya")
                    with sr.Microphone() as source:
                        print("Jarvis Active..!! ")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
    


