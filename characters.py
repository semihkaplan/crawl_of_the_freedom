class Character:
    def __init__(self, cName, cGender, cClass):
        self.cName = cName
        self.cCender = cGender
        self.cClass = cClass


def create_player():
    pName = input("\nWhat is your name adventurer?: ")

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

    player = Character(pName, pGender, pClass)
