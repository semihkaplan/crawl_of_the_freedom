import engine
import sys
from time import sleep
from colorama import Fore, Back, Style


def intro():
    intro = open("intro.txt", "r", encoding="utf8")
    print(Fore.RED + intro.read() + Style.RESET_ALL)
    intro.close()


def story_telling():
    story = open("story.txt", "r", encoding="utf8")
    story_color = Fore.YELLOW + story.read()+ "\n" + Style.RESET_ALL
    story.close()

    engine.typewriter(story_color, 0.05)
