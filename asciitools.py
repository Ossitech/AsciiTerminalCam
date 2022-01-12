import os
import sys

def runCommand(command):
 with os.popen(command) as p:
  result = p.read()

 return result

def getTerminalSize():
 width = int(runCommand("tput cols"))
 height = int(runCommand("tput lines"))

 return (width, height)

def setCursorPos(x, y):
 sys.stdout.write(f"\033[{y};{x}H")

def clearScreen():
 sys.stdout.write("\033[2J")

def clearLine():
 sys.stdout.write("\033[2K")

def setForegroundColor(r, g, b):
 sys.stdout.write(f"\033[38;2;{r};{g};{b}m")

def setBackgroundColor(r, g, b):
 sys.stdout.write(f"\033[48;2;{r};{g};{b}m")
