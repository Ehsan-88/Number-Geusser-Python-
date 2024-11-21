import random
from colorama import Fore, Style, init

init(autoreset=True)

def guess_number():
    number = random.randint(1, 10)
    attempts = 0

    print(Fore.CYAN + "Welcome to the Number Guessing Game!")
    print(Fore.CYAN + "A number between 1 and 10 has been chosen. Identify it.")

    while True:
        try:
            guess = int(input(Fore.YELLOW + "Enter your guess: "))
            attempts += 1

            if guess < number:
                print(Fore.RED + "Too low! Try again.")
            elif guess > number:
                print(Fore.RED + "Too high! Try again.")
            else:
                print(Fore.GREEN + f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break

        except ValueError:
            print(Fore.MAGENTA + "Invalid input. Please enter an integer.")

guess_number()
