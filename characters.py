import engine
import keyboard
from time import sleep

class Character:
    def __init__(self, cName, cGender, cClass, cStats):
        self.cName = cName
        self.cCender = cGender
        self.cClass = cClass


def create_player():
    while True:
        pName = input("\nWhat is your name adventurer?: ")
        
        if pName == '':
            print("\nI asked your name dumbass!")

        else:
            break

    stupid = False

    while True:
        pGender = input("\nAre you a man or a woman? [man/woman]: ")

        if pGender.lower() == "man":
            print("\nYeah, obviously you're a man. But I had to ask. You know, you can't be sure these times.")
            break

        elif pGender.lower() == "woman":
            print("\nOf course. I didn't mean you look like a man. Actually, I gotta admit, you are a very attractive woman.")
            break

        else:
            print("\nThere are no more than two genders, you faggot!")
            stupid = True
    
    while True:
        pClass = input("\nAnd what is your class? I mean what are you good at? [warrior/ranger/mage]: ")
        
        if pClass.lower() in ("warrior", "ranger", "mage"):
            print("\nA good class. I guess.")
            break

        else:
            if stupid:
                print("\nYou're retarded, aren't ya?")
            
            else:
                print("\nI asked a simple question. Please answer to me seriously.")
                stupid = True


def set_stats():
    strength = intelligence = dexterity = 1
    points = 3

    while points >= 0:
        engine.clear()
        print(
        """
        SET YOUR STATS

        1 - Strength: {}
        2 - Intelligence: {}
        3 - Dexterity: {}

        """.format(strength, intelligence, dexterity))

        while points > 0:
            print("Press the button, which is the number of the statistic you want to increase.")

            if keyboard.read_key() == '1':
                strength += 1
                break

            elif keyboard.read_key() == '2':
                intelligence += 1
                break

            elif keyboard.read_key() == '3':
                dexterity += 1
                break

            else:
                points += 1
                break

        points -= 1
        sleep(0.1)
