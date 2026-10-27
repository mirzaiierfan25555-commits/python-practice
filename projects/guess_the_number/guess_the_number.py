
import random


class GuessNumber:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.a = 1
        self.b = difficulty
        self.rand = random.randint(self.a, self.b)
        self.max_tries = 7
        self.tries = 0

    def play(self):
        print(f"\nGuess a number between {self.a} and {self.b}")
        print(f"You have {self.max_tries} attempts.")

        while self.tries < self.max_tries:
            try:
                choose = int(input("Enter your guess: "))

                if choose < self.a or choose > self.b:
                    print(f"Enter a number between {self.a} and {self.b}.")
                    continue

            except ValueError:
                print("Please enter a valid integer!")
                continue

            self.tries += 1

            if choose == self.rand:
                print("Ohh! You win!")
                print(f"You guessed it in {self.tries} attempts.")
                return

            elif choose > self.rand:
                print("My number is smaller.")
                self.b = choose - 1

            else:
                print("My number is bigger.")
                self.a = choose + 1

            print(f"Choose between {self.a} and {self.b}")
            print(f"Attempts left: {self.max_tries - self.tries}")

        print(f"\nGame over! My number was {self.rand}.")


def main():
    while True:
        difficulty = input(
            "Choose difficulty: 1. Easy (1-50)  "
            "2. Medium (1-100)  3. Hard (1-500): "
        ).strip()

        if difficulty == "1":
            max_number = 50
            break
        elif difficulty == "2":
            max_number = 100
            break
        elif difficulty == "3":
            max_number = 500
            break
        else:
            print("Please enter 1, 2, or 3.")

    game = GuessNumber(max_number)
    game.play()


if __name__ == "__main__":
    main()
