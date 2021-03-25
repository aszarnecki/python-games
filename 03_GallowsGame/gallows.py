import random
import os

GALLOWS_PICS = [
    '''
     +___+
         |
         |
         |
        ===
    ''',
    '''
     +___+
     o   |
         |
         |
        ===
    ''',
    '''
     +___+
     o   |
     |   |
         |
        ===
    ''',
    '''
     +___+
     o   |
    \|   |
         |
        ===
    ''',
    '''
     +___+
     o   |
    \|/  |
         |
        ===
    ''',
    '''
     +___+
     o   |
    \|/  |
    /    |
        ===
    ''',
    '''
     +___+
     o   |
    \|/  |
    / \  |
        ===
    '''
]


class GallowsGame:
    def __init__(self):
        self.wrong_answers_counter = 0
        self.answers = []
        self.hidden_password = list(GallowsGame.__get_password())
        self.visible_password = list("_" * len(self.hidden_password))
        self.error = ""

    def play(self):
        while self.wrong_answers_counter != 6 and self.hidden_password != self.visible_password:
            print('S Z U B I E N I C A')
            if self.error:
                print(self.error)
            print(GALLOWS_PICS[self.wrong_answers_counter])
            print(f"HASLO: {' '.join(self.visible_password)}")
            print(f"Wybrane litery: {', '.join(self.answers)}")
            answer = input("PODAJ LITERE: ").upper()
            if len(answer) != 1 or answer.isdigit():
                self.error = 'Podaj litere'
            elif answer in self.answers:
                self.error = 'Wybrana litera byla juz uzyta'
            elif answer in self.hidden_password:
                self.answers.append(answer)
                indexes = [i for i, x in enumerate(self.hidden_password) if x == answer]
                for i in indexes:
                    self.visible_password[i] = answer
            else:
                self.answers.append(answer)
                self.wrong_answers_counter += 1
            GallowsGame.cls()
        if self.wrong_answers_counter == 6:
            self.print_lose()
        else:
            self.print_win()

    def print_lose(self):
        print('P R Z E G R A L E S')
        print(GALLOWS_PICS[6])
        print(f'POPRAWNE HASLO: {"".join(self.hidden_password)}')

    def print_win(self):
        print('G R A T U L A C J E')
        print(GALLOWS_PICS[self.wrong_answers_counter])
        print(f'ODGADLES POPRAWNE HASLO: {"".join(self.hidden_password)}')
        print(f"LICZBA BLEDNYCH ODPOWIEDZI: {self.wrong_answers_counter}")

    @staticmethod
    def cls():
        os.system('cls')

    @staticmethod
    def __get_password():
        with open('password.txt', 'r', encoding='utf-8') as f:
            passwords = f.read().split(';')
        return random.choice(passwords)


if __name__ == "__main__":
    game = GallowsGame()
    game.play()
