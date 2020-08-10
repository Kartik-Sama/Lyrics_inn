import speech_recognition
import sys
import os


def get_input():

    try:
        recognizer = speech_recognition.Recognizer()
        sys.stdout = open(os.devnull, 'w')
        with speech_recognition.Microphone() as source:
            audio = recognizer.listen(source)
            myinp = recognizer.recognize_google(audio)
        sys.stdout = sys.__stdout__        

        print("\nGoogle Speech Recognition thinks you said:")
        print(myinp)

    except:
        sys.stdout = sys.__stdout__
        print("\nERROR!!!\nCould not detect sound/microphone! Please enter the song name using keyboard:")
        myinp = input()
        
    return myinp