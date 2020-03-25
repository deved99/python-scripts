#!/usr/bin/env python
from os import listdir, devnull
import subprocess
import mutagen.id3
import mutagen.flac

def qRun(command):
    with open(devnull) as redir:
        subprocess.run(
            command,
            stdout = redir,
            stderr = redir)

def convert(song):
    print("Converting "+song+" to mp3")
    newsong = song[:song.rfind(".")]+".mp3"
    command = [
        "ffmpeg",
        "-i", song,
        "-ab", "320k",
        newsong
    ]
    qRun(command)
    qRun(["rm", song])
    return newsong

artist = input("Artist? ")
album = input("Album? ")
year = input("Year? ")

print("")
files = listdir("./")
songs = []
cover =[]
for f in files:
    ext = f[ f.rfind('.')+1 :]
    if ext in ["mp3"]:
        songs.append(f)
    elif ext in ["flac", "m4a"]:
        newf = convert(f)
        songs.append(newf)
    elif "cover" in f:
        cover.append(f)

print("\nUpdating tags:")
for song in songs:
    print(song)
    k = song.find(' ')
    l = song.rfind('.')
    # Find track number and title
    num = song[:k]
    title = song[k+1:l]

    # Set tags
    tags = mutagen.id3.ID3()
    tags["TALB"] = mutagen.id3.TALB(text=album)
    tags["TDRC"] = mutagen.id3.TDRC(text=year)
    tags["TIT2"] = mutagen.id3.TIT2(text=title)
    tags["TPE1"] = mutagen.id3.TPE1(text=artist)
    tags["TRCK"] = mutagen.id3.TRCK(text=num)
    if len(cover) == 1:
        tags["APIC"] = mutagen.id3.APIC(
            mime="image/jpeg",
            data=open(cover[0], 'rb').read()
        )
    # Save tags
    tags.save(song)

if len(cover) != 1:
    print("\nProblems with cover")
