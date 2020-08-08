import speech_recognition

import os

def speech_input_check():
    try:
        sys.stdout = open(os.devnull, 'w')
        speech_recognition.Recognizer()
        speech_recognition.Microphone()
        sys.stdout = sys.__stdout__
        return True
    except:
        return False

def speech_user_input():
    # DEMO
    recognizer = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as source:
        print("Speak up we are listening")
        audio = recognizer.listen(source)
    myinp = recognizer.recognize_google(audio)
    print("Google Speech Recognition thinks you said:",myinp)
    return myinp
    