import random


def guess(x):
    randum_numbers = random.randint(1, x)
    guess = 0
    while guess != randum_numbers:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < randum_numbers:
            print("Sorry, guess again. Too low.")
        elif guess > randum_numbers:
            print("Sorry, guess again. Too high.")

    print(f"Yay, congrats. You have guessed the number {randum_numbers} correctly!")


guess(10)
