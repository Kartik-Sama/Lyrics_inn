# Make HTTP requests
import requests
# I/O
import os
# Scrape data from an HTML document
from bs4 import BeautifulSoup
# Search and manipulate strings
import re

GENIUS_API_TOKEN = 'NN3ws9rZorqMaFGlHNmeUR7RjtaWirQBrB8n5EmTBQUe_K-JALxgu-ArM8zAMyJ9'

# Get query object from Genius API
def request_song_info(song_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': song_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response
# Get Genius.com song url's from artist object
def request_song_url(song_name, song_cap=10):
    page = 1
    songs = []
    
    while True:
        response = request_song_info(song_name, page)
        json = response.json()
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            songTitle = hit['result']['full_title']
            for s in song_name.lower():
                if s in songTitle:
                    print_top_results(songTitle, hit)
                    song_info.append(hit)
                    break
    
        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)
            
        if (len(songs) >= song_cap):
            break
        else:
            page += 1
        
    return songs


def print_top_results(songTitle, hit):
    songTitle = songTitle.lstrip()
    songTitle = (songTitle[:57]+"...") if len(songTitle) > 60 else songTitle
    print(songTitle, (65-len(songTitle))*" ", "-", 10*" ", hit['result']['primary_artist']['name'])

def song_lyrics(song):
    songs_url = request_song_url(song)
    url = songs_url[0]
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics1 = html.find("div", class_="lyrics")
    lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
    if lyrics1:
        lyrics = lyrics1.get_text()
    elif lyrics2:
        lyrics = lyrics2.get_text()
    elif lyrics1 == lyrics2 == None:
        lyrics = None
    #remove identifiers like chorus, verse, etc
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '\n', lyrics)
    #remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])         
    #print(lyrics)