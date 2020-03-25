#!/usr/bin/env python
import sys
from subprocess import run
from shutil import copy
from os import mkdir, chdir
from os.path import isdir

def texcompile(filename):
    if not isdir(".out/"):
        mkdir(".out/")
    command = [
            "latexmk", "-pdf", "-f",
            "-outdir=.out/",
            filename
            ]
    proc = run(command)
    # the filename should be something.tex
    # hence filename[:-3] is something.
    outpdf = filename[:-3]+"pdf"
    if proc.returncode == 0:
        copy(".out/"+outpdf, outpdf)

if len(sys.argv) == 2:
    fpath = sys.argv[1]
    if "/" in fpath:
        k = fpath.rfind("/")+1
        folder = fpath[:k]
        filename = fpath[k:]
    else:
        folder = "./"
        filename = fpath

    if isdir(folder):
          chdir(folder)
          texcompile(filename)
    else:
        print("Folder not found")
else:
    print("Exactly one argument, the filename.")
