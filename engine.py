import os
import sys
from time import sleep
from playsound import playsound


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


def typewriter_sound():
    playsound("typewriter.wav")
