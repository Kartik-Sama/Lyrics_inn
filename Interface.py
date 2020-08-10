# Make HTTP requests
import requests
# I/O
import os
# Search and manipulate strings
import re

from Scrap_Lyrics_URL import song_lyrics
from speech_enabled import get_input


# Check if user has microphone access and take input from text if not.
Song = get_input()

song_lyrics(Song)
