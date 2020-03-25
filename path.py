#!/usr/bin/env python
import sys
import subprocess
from os.path import expanduser

if len(sys.argv) == 3:
    if sys.argv[1] == "add":
        f = sys.argv[2]
        if '.' in f:
            dest = f[:f.find('.')]
        else:
            dest = f

        commands = [
            ["chmod", "+x", f],
            ["cp", f, expanduser("~/.local/bin/")+dest]
        ]
        for command in commands:
            subprocess.run(command)
    elif sys.argv[1] == "del":
        f = sys.argv[2]
        command = ["rm", expanduser("~/.local/bin/")+f]
        subprocess.run(command)
else:
    print("This command need 2 arguments: option and file")
    print("options:")
    print("add \t add file to path")
    print("del \t delete file from path")
