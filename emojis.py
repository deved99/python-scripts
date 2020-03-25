#!/usr/bin/env python
from os.path import expanduser
from subprocess import Popen, check_output, PIPE

# Find emojis list file
emoji_src = expanduser(
        "~/Coding/Scripts/emojis")
# Pass it to rofi
cat_emoji = Popen(
        ["cat", emoji_src],
        stdout=PIPE)
emoji = check_output(
        ["rofi", "-dmenu", "-i", "-p", "emojis"],
        stdin = cat_emoji.stdout).decode('utf8')
# Convert to unicode and retain only 
# emoji
k = emoji.find(" ")
emoji = emoji[:k]

# Insert the emoji
insertEmoji = [
        "xdotool", "type",
        "--clearmodifiers",
        emoji]
Popen(insertEmoji)
