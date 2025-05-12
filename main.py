"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Oleg Eremenko
email: eremenko.oleg26@gmail.com
"""
# Bulls & Cows
# Hra pro jednoho hráče, kde hráč hádá tajné 4místné číslo

import random
import time


def generate_secret_number():
    """Generuje tajné 4místné číslo s unikátními číslicemi nezačínající nulou"""
    while True:
        digits = random.sample('0123456789', 4)
        if digits[0] != '0':
            return ''.join(digits)


def validate_guess(guess):
    """Ověřuje uživatelský vstup"""
    if not guess.isdigit():
        return "Enter only numbers."
    if len(guess) != 4:
        return "The number must have exactly 4 digits."
    if guess[0] == '0':
        return "The number must not start with a zero."
    if len(set(guess)) != 4:
        return "All digits must be unique."
    return None


def count_bulls_and_cows(secret, guess):
    """Spočítá bulls a cows"""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def format_result(bulls, cows):
    """Formátuje výsledek s ohledem na jednotné/množné číslo"""
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_text}, {cows} {cow_text}"


def format_time(seconds):
    """Počítá čas, za jak dlouho uživatel uhádne tajné číslo"""
    minutes, seconds = divmod(int(seconds), 60)
    if minutes > 0:
        return f"{minutes}m {seconds}s"
    return f"{seconds}s"


def play_game():
    """Hlavní funkce pro hru"""
    secret = generate_secret_number()
    attempts = 0
    start_time = time.time()

    print("\nHi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    while True:
        print("Enter a number:")
        print("-" * 47)
        guess = input(">>> ").strip()

        error = validate_guess(guess)
        if error:
            print(error)
            print("-" * 47)
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret, guess)

        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            time_str = format_time(elapsed_time)

            print(f"Correct, you've guessed the right number")
            print(f"in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            print("-" * 47)
            print(f"Game time: {time_str}")
            print("-" * 47)

            if attempts <= 5:
                print("That's amazing!\n")
            elif attempts <= 10:
                print("That's good!\n")
            else:
                print("Not bad!\n")
            break
        else:
            print(format_result(bulls, cows))
            print("-" * 47)


if __name__ == "__main__":
    play_game()




