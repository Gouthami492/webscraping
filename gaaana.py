#Python Program for extracting data using web scraping i.e the top English songs in 2020  on Gaana.
from bs4 import BeautifulSoup
import requests

data=requests.get("https://gaana.com/playlist/arkabanerjee-whxhx-topenglishsongs")
soup=BeautifulSoup(data.text,"html.parser")

header=['Serial No','Title','Artist(s)']
songs=[]

artist_tag=soup.find_all("a","sng_c")
#artist_tag=soup.find_all("li","sng_c")
title_tag=soup.find_all("div","track_npqitemdetail")

serial_no=[]
title=[]
artists=[]

print(header)

for i in range(0,len(title_tag)):
    serial_no.append(i+1)
    title.append(title_tag[i].span.text)
    #artists.append(artist_tag[i]..text)
    song=[]
    song.append(serial_no[i])
    song.append(title[i])
    #song.append(artists[i])
    songs.append(song)

for song in songs:
    print(song)
