#!/usr/bin/env python
from os import listdir, rename, makedirs
from os.path import isdir, expanduser
from subprocess import run, Popen
editor = "nvim"
trash = expanduser("~/.local/trash/")

def move(oldfile, newfile):
    if "/" in newfile:
        k = newfile.rfind("/")
        folder = newfile[:k]
        if not isdir(folder):
            makedirs(folder)
    rename(oldfile, newfile)

def getnames(files):
    tmp_file = "/tmp/bulkrename"

    text = files[0]
    for file in files[1:]:
        text = text +"\n"+file
    with open(tmp_file, "w") as f:
        f.write(text)

    run([editor, tmp_file])
    files_new = []
    with open(tmp_file, "r") as f:
        for line in f.readlines():
            files_new.append(line[:-1])

    Popen(["rm", tmp_file])
    return files_new


files = sorted(listdir())
files_new = getnames(files)
n = len(files)

if len(files_new) == n:
    for i in range(0, n):
        if files_new[i] == "rm":
            move(files[i], trash+files[i])
        else:
            if files[i] != files_new[i]:
                move(files[i], files_new[i])
else:
    print("The numbers of new files is changed.")
