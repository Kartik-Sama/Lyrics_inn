import speech_recognition
import sys
import os
from ctypes import *

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  print("",end="")

if sys.platform == "linux" or sys.platform == "linux2":
    c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)

def get_input():
    
    try:    
        recognizer = speech_recognition.Recognizer()
        microphone = speech_recognition.Microphone()
        print("Speak Out! We are listening!")
        with microphone as source:
            audio = recognizer.listen(source)
            myinp = recognizer.recognize_google(audio)
            print("\nGoogle Speech Recognition thinks you said:")
            print(myinp)
    except OSError:
        print("\nERROR: Could not detect connect to microphone!")
        myinp = input("Please enter the song name using keyboard :\n")

    except speech_recognition.UnknownValueError:
        print("\nERROR: Couldn't recognize what you said!")
        myinp = input("Please enter the song name using keyboard :\n")
    
    except Exception as e:
        print("\n", e, sep='\n')
        myinp = input("Please enter the song name using keyboard :\n")
        
    return myinp
