from icecream import ic


class GameConfig:
    MAX_LEVEL = 100
    SERVER_NAME = "Stepik-RPG"


def main():
    my_config = GameConfig()
    ic(my_config)
    ic(my_config.MAX_LEVEL)
    ic(my_config.SERVER_NAME)

if __name__ == "__main__":
    main()