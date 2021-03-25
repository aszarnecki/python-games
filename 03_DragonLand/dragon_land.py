import random
import time


class DragonLandGame:
    @staticmethod
    def play() -> None:
        want_play = True
        while want_play:
            DragonLandGame.__print_intro()
            cave = DragonLandGame.__choose_cave()
            DragonLandGame.__check_cave(cave)

            print("Chcesz zagrać ponownie? (tak/nie)")
            want_play = 't' in input().lower()


    @staticmethod
    def __print_intro() -> None:
        print("Znajdujesz się w krainie smoków. Przed sobą widzisz dwie jaskinie. "
              "W jednej mieszka przyjazny smok, który podzieli się z tobą swoim skarbem. "
              "Drugi smok jest chciwy i głodny, więc pożre Cię bez zmrużenia oka.\n")

    @staticmethod
    def __choose_cave() -> int:
        cave = None
        while cave != 1 and cave != 2:
            print("Do której jaskini chcesz wejść? (1 lub 2)")
            cave = int(input())

        return cave

    @staticmethod
    def __check_cave(cave: int) -> None:
        print('Zbliżasz się do mrocznej jaskini...')
        time.sleep(2)
        print('Wtem! Nagle! Raptem!')
        time.sleep(2)
        print('Pojawia się straszliwy smok... Otwiera swoją paszcczę i...')
        time.sleep(2)
        positive_cave = random.randint(1, 2)
        if cave == positive_cave:
            print('Oddaje ci swój skarb!')
        else:
            print("Mniam, mniam! Pożera cię w całości")


if __name__ == "__main__":
    game = DragonLandGame()
    game.play()
