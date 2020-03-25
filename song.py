#!/usr/bin/env python
from mpd import MPDClient
from os.path import expanduser
import sys
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify  # noqa: E402

musicdir = expanduser("~/Music/")
client = MPDClient()
client.connect("localhost", 6600)

if len(sys.argv) == 2:
    print("hi")

song = client.currentsong()
title = song["title"]
artist = song["artist"]
filepath = song["file"]
k = filepath.rfind("/")
cover = musicdir + filepath[:k] + "/cover.jpg"

Notify.init("MPD Song")
cursong = Notify.Notification.new(title, artist, cover)
cursong.show()
