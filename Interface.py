# Make HTTP requests
import requests
# I/O
import os
# Search and manipulate strings
import re

from Scrap_Lyrics_URL import song_lyrics
from speech_enabled import *

# Artist
Audio_Input = speech_input_check()
if(not Audio_Input):
    print("Audio input couldn't be connected. Please make sure to install SpeechRecognition module and PyAudio to use search by speech option.")

Song = input("Enter the song : ")
song_lyrics(Song)