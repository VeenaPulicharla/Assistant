import speech_recognition as sr  # import the library
import pyttsx3
import os

r = sr.Recognizer()  # initialize recognizer
with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)  # listen to the source
    try:
        text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")


    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Error: some pyttsx error")
        engine.say('Module error')
        engine.runAndWait()





# Pygame
# https://stackoverflow.com/questions/51164040/gtts-direct-output
# https://stackoverflow.com/questions/16325794/how-to-play-music-through-python-with-mpg321