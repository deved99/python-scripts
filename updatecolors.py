#!/usr/bin/env python
import sys
from os import chdir, devnull
from os.path import expanduser
import subprocess

def grepSkel(conf0):
    with open(conf0, 'r') as conf:
        config = conf.readlines()
    return config

def subConf(config, subs):
    k = len(config)-1
    for i in range(0,k):
        line = config[i]
        for orig,new in subs.items():
            line = line.replace(
                orig, new
            )
        config[i] = line
    return config

def saveConf(config, dest):
    with open(dest, 'w') as conf:
        for line in config:
            conf.write(line)

def initCmds(commands):
    with open(devnull,"w") as redir:
        for command in commands[:-1]:
            proc = subprocess.run(
                command,
                stdout=redir,
                stderr=redir
            )
            if proc.returncode != 0:
                print("Problems with: "+" ".join(command))
        subprocess.Popen(
            commands[-1],
            stdout=redir,
            stderr=redir
        )

def addlight(commands,opt):
    if len(opt) > 1:
        if opt[1:] == "l":
            commands[1].append("-l")
        else:
            print("Check 2nd arg")


home = expanduser("~/")
homeConf = home+".config/"

chdir(home)
if len(sys.argv) == 3:
    opt = sys.argv[1]
    color_src = sys.argv[2]

    commands = [
        ["wal", "-c"],
        [],  # depends on options
        ["cp",
         ".cache/wal/colors",
         ".config/colors"]
    ]
    if opt[0] == "i":
        commands[1] = ["wal", "-i", color_src]
        addlight(commands, opt)
    elif opt[0] == "t":
        commands[1] = ["wal", "--theme", color_src]
        addlight(commands, opt)
    for command in commands:
        subprocess.run(command)
elif len(sys.argv) > 1:
    print("Either no argument or exactly 2")

chdir(homeConf)
colors = []
with open("colors", 'r') as src:
    for color in src.readlines():
        colors.append(color[:-1])

background = colors[0]
white = colors[7]
theme = colors[2]
red = colors[1]

print("Updating Alacritty")
config = grepSkel("alacritty/alacritty0.yml")
subs = {}
for i in range(0, 16):
    subs["'color"+str(i)+"'"] = "'"+colors[i]+"'"
config = subConf(config, subs)
saveConf(config, "alacritty/alacritty.yml")

print("Updating Dunst")
config = grepSkel("dunst/dunstrc0")
subs = {
    "bg_color": background,
    "fg_color": theme
}
config = subConf(config, subs)
saveConf(config, "dunst/dunstrc")
commands = [
    ["killall", "dunst"],
    ["dunst"]
]
initCmds(commands)

print("Updating Rofi")
config = grepSkel("rofi/theme0.rasi")
opacity = "bf"  # alpha
subs = {
    "blackbg": background+opacity,
    "black": background,
    "grey": theme,
    "white": white,
    "red": red
}
config = subConf(config, subs)
saveConf(config, "rofi/theme.rasi")

print("Updating Zathura")
config = grepSkel("zathura/zathurarc0")
subs = {
    "bg_color": background,
    "fg_color": white,
    "red_color": red,
    "theme_color": theme
}
config = subConf(config, subs)
saveConf(config, "zathura/zathurarc")

print("Updating XMonad")
config = grepSkel("xmonad/xmonad0.hs")
subs = {
    "theme_color": theme,
    "fg_color": white
}
config = subConf(config, subs)
saveConf(config, "xmonad/xmonad.hs")
commands = [
    ["xmonad", "--recompile"],
    ["xmonad", "--restart"]
]
initCmds(commands)

chdir(home)
print("Updating wallpaper")
commands = [
        ["convert", "Pictures/Cats/Simon's Cat - Cat Sleeping.jpg",
            "+level-colors", background+","+white,
            ".bg.jpg"],
        ["feh", "--bg-fill", ".bg.jpg"]
        ]
initCmds(commands)
