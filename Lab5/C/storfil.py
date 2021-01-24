# Written by Christian Abdelmassih, Alexandra Runhem

from time import *
from hashtabell import *

def lasfil(filnamn):
    f = open(filnamn, encoding="UTF-8")
    h_tabell = Hashtabell(len(f.readlines()))
    f.close()

    with open(filnamn, encoding="UTF-8") as fil:
        for rad in fil:
            data = rad.split("<SEP>")
            artist = data[2].strip()
            song = data[3].strip()

            nod = Node(artist, song)
            h_tabell.put(artist, nod)
    return h_tabell

def hitta(artist, h_table_obj):
    start = time()
    print(h_table_obj.get(artist))
    tidhash = str(round(time() - start,10))
    return tidhash

start = time()
h_tabell = lasfil("unique_tracks.txt")
print("Table Done",str(round(time() - start)))

artist = "Elude"
tidhash = hitta(artist, h_tabell)
print("Time for accessing", artist, tidhash, "sec")