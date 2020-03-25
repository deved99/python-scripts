#!/usr/bin/env python
import subprocess
from os.path import expanduser

commands = [
    ["feh", "--bg-fill", expanduser("~/.bg.jpg")],
    ["xsetroot", "-cursor_name", "left_ptr"],
    ["mpd"],
    ["dunst"],
    ["flameshot"],
    ["picom", "--experimental-backends"]
]
for command in commands:
    subprocess.Popen(command)

controls = [
    ["checkbat"],
]
while True:
    for command in controls:
        subprocess.Popen(command)
    subprocess.run(["sleep", "1m"])
