import engine
import texts
import characters


def main():
    engine.clear()
    texts.intro()
    texts.story_telling()
    characters.create_player()
    characters.set_stats()


if __name__ == "__main__":
    main()
