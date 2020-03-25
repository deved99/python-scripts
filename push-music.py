#!/usr/bin/env python
import subprocess, sys
from os.path import expanduser

music = expanduser("~/Music/")
if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as source:
        lines = source.readlines()
    for line in lines:
        command = [
            "adb", "push",
            
        ]    
