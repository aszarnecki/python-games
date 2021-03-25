import random


class GuessNumberGame:
    def __init__(self):
        self.number = random.randint(1, 20)
        self.player_name = GuessNumberGame.__get_player_name()
        self.answers_count = 0

    def play(self):
        print(f"Słuchaj, {self.player_name}, myślę o liczbie z przedziału od 1 do 20")
        while True:
            print("Spróbuj odgadnąć")
            player_answer = int(input())
            self.answers_count += 1
            if player_answer > self.number:
                print("Twoja liczba jest za duża")
                continue
            elif player_answer < self.number:
                print("Twoja liczba jest za mała")
                continue
            else:
                print(f"Świetna robota, {self.player_name}! Udało Ci się odgadnąć w {self.answers_count} próbach")
                break

    @staticmethod
    def __get_player_name() -> str:
        print("Hej! Jak masz na imię?")
        name = input()
        return name


if __name__ == "__main__":
    game = GuessNumberGame()
    game.play()
