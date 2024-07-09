#   Finding word frequences in the given url

import requests
import operator
from bs4 import BeautifulSoup

################################################

def sozluk_olustur(tumkelimeler):
    kelimesayisi = {}
    for kelime in tumkelimeler:
        if(kelime in kelimesayisi): 
            kelimesayisi[kelime] += 1
        else:
            kelimesayisi[kelime] = 1
    return kelimesayisi
    
################################################

def sembolleri_sil(tum_kelimeler):
    sembolsuz = []
    semboller ="!@$#^'*()+_-[]<>?,':;.=\"/`´"

    for kelime in tum_kelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")

        if(len(kelime)> 0):
            sembolsuz.append(kelime)

    return sembolsuz

################################################

url = "https://tr.wikipedia.org/wiki/Giresun"

tum_kelimeler = []

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

for kelimegruplari in soup.find_all("p")[1:]:
    #print(kelimegruplari)
    icerik = kelimegruplari.text
    kelimeler = icerik.lower().split()

    #print(kelimeler)

    for kelime in kelimeler:
        tum_kelimeler.append(kelime)
        #print(kelime)

tum_kelimeler = sembolleri_sil(tum_kelimeler)
kelime_sayisi = sozluk_olustur(tum_kelimeler)

#for kelime in tum_kelimeler:
    #print(kelime)

for anahtar,deger in sorted(kelime_sayisi.items(),key = operator.itemgetter(1),reverse=True):
    print(anahtar,deger)

