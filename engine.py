import os
import sys
from time import sleep


def clear():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def typewriter(text, speed):
    for char in text:
        sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()
