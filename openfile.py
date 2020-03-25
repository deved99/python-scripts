#!/usr/bin/env python
from os import getcwd, devnull
from os.path import expanduser, abspath
import subprocess
import sys

# Quietly exec command
def qPopen(command):
    with open(devnull, 'w') as redir:
        subprocess.Popen(command,
                         stdout=redir,
                         stderr=redir)

def openfile(filename,folder):
    # First find the file's extension
    if "." in filename:
        ext = filename[ filename.rfind('.')+1 :]
    else:
        # If there's no dot in the filename
        # either it is a plain text file or
        # it is a folder. In both cases I
        # want to open it in emacs
        ext = "else"

    # Now exec commands depending on ext
    if ext in ["mp3","flac"]:
        k = len(expanduser("~/Music/"))
        mdir = folder[k:]
        ntrack = int(filename[ :filename.find(" ")])
        commands = [
            ["mpc", "-q", "clear"],
            ["mpc", "add", mdir],
            ["mpc", "-q", "searchplay", "Track", str(ntrack)]
            ]
        for command in commands:
            subprocess.run(command)
    elif ext in ["pdf","djvu","epub"]:
        command = ["zathura", folder+filename]
        qPopen(command)
    elif ext in ["mkv","mp4","webm"]:
        command = ["mpv", folder+filename]
        qPopen(command)
    elif ext in ["png","jpg","jpeg"]:
        command = ["feh", "-Z", folder, "--start-at", filename]
        qPopen(command)
    else:
        command = ["alacritty",
                "--class", "Editor",
                "-e", "nvim", folder+filename]
        qPopen(command)

if len(sys.argv) == 2: # exactly one argument
    tmp = str(sys.argv[1])

    if tmp[0] != "/": # If not absolute path
        if tmp[0] == "~":
            # expand ~ to $HOME in case
            tmp = expanduser(tmp)
        else:
            tmp = abspath(getcwd())+"/"+tmp

    k = tmp.rfind('/')+1
    # If the last word of the argument is a folder
    # without a final slash, the file will be the
    # folder's name
    folder = tmp[:k]
    filename = tmp[k:]
    openfile(filename,folder)
else:
    print("One and only one argument")
