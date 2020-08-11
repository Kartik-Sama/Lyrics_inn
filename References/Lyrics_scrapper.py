import requests
from bs4 import BeautifulSoup
import os
import re

GENIUS_API_TOKEN = 'NN3ws9rZorqMaFGlHNmeUR7RjtaWirQBrB8n5EmTBQUe_K-JALxgu-ArM8zAMyJ9'

# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response

# Get Genius.com song url's from artist object
def request_song_url(artist_name, song_cap):
    page = 1
    songs = []
    
    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        # print(json)
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:

            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)
    
        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)
            
        if (len(songs) == song_cap):
            break
        else:
            page += 1
        
    print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs
    
# DEMO
songs_url = request_song_url('Ed Sheeran', 1)

def request_song_url_by_song_name(song, song_cap):
    page = 1
    songs = []
    
    while True:
        response = request_artist_info(song, page)
        json = response.json()
        # print(len(json['response']['hits']))
        # print(json)
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if song.lower() in hit['result']['title'].lower():
                song_info.append(hit)
        # print(len(song_info))
        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)
        if (len(songs) == song_cap):
            break
        else:
            page += 1
        
    print('Found')
    return songs
songs_url1 = request_song_url_by_song_name('Shape of You', 1)
print(songs_url,songs_url1)
# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(url):
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
        return "Lyrics not found. Please check the song name and title."
    print(lyrics)
    #remove identifiers like chorus, verse, etc
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '\n', lyrics)
    #remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])         
    return lyrics
# DEMO
# print(scrape_song_lyrics(songs_url[0]))
print(scrape_song_lyrics(songs_url[0]))