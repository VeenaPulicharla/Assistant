import speech_recognition as sr
from time import ctime
from gtts import gTTS
import pyttsx3
import os
import random
import webbrowser
import urllib
import urllib.request
import urllib.parse
import json as m_json

# Pygame
# https://stackoverflow.com/questions/51164040/gtts-direct-output
# https://stackoverflow.com/questions/16325794/how-to-play-music-through-python-with-mpg321

def speak(audio_text):
    """
    Speaks out
    :param audio_text:
    :return:
    """
    print(audio_text)
    tts = gTTS(text=audio_text)
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")


def record_audio():
    """
    Listens to audio
    :return:
    """
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        # print("Speak Anything :")
        speak("speak anything")
        audio = r.listen(source)  # listen to the source
    text = ""
    try:
        text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
    except sr.UnknownValueError:
        error_msg = "I couldn't understand or hear you properly"
        print(error_msg)
        speak(error_msg)
    except sr.RequestError as e:
        error_msg = "Could not request results form Speech recognition service"
        print(error_msg+"{0}".format(e))
        speak(error_msg)
    return text


def ai(text):
    if ("What id your name") in text:
        speak("I am Eesha, Nice to meet you!")

    if ("hi Esha" in text) or ("hi in eesha" in  text) :
        speak("Hey!")

    if ("hello Esha" in text) or ("hello Eesha" in text):
        speak("hello")

    if "hello" in text:
        speak("Hai")

    if ("hai" in text) or ("hi" in text):
        speak("Hello")

    if "tell my colleagues I am innocent" in text:
        speak("No, you are not")

    if ("where is" in text) or ("show me" in text):
        text = text.split()
        location = text[2]
        speak("hold on a second, here is the map for"+location)
        webbrowser.open('https://www.google.co.in/maps/place/'+location+"/&amp;")
        # os.system("chromium-browser https://www.google.co.in/maps/place/" + location + "/&amp;")

    if ("what is") in text or ("show me") or ("What does")in text:
        search_term  = text
        url = "https://www.google.com.tr/search?q={}".format(search_term)
        webbrowser.open(url)
    if ("what is your number") or ("what's your number") in text:
        temp_strings = ["Sorry, I am not interested", "0 1","Ask Dinesh"]
        speak(random.choice(temp_strings))


def main():
    welcome_strings = ["Hai, I am Eesha, what can I do for you ?", "Hello, This is Eesha, what can I do for you",
                       "Hey, I am Eesha, Nice to meet you"]
    speak(random.choice(welcome_strings))
    while True:
        data = record_audio()
        ai(data)


if __name__ == '__main__':
    main()