import engine
import sys
from time import sleep
from multiprocessing import Process
from colorama import Fore, Back, Style


def intro():
    intro = open("intro.txt", "r", encoding="utf8")
    print(Fore.RED + intro.read() + Style.RESET_ALL)
    intro.close()


def story_telling():
    story = open("story.txt", "r", encoding="utf8")
    story_color = Fore.YELLOW + story.read()+ "\n\n" + Style.RESET_ALL
    story.close()
    
    writing = Process(target=engine.typewriter, args=(story_color, 0.001))
    sound = Process(target=engine.typewriter_sound)
    
    writing.start()
    sound.start()
    writing.join()
    sound.join()

    input(Fore.RED + "Press ENTER key to continue..." + Style.RESET_ALL)
    engine.clear()
