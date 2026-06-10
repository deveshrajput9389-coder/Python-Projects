import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    # Generate a random number
    winnng_number = random.randint(1, 100)
    attempt = 0

    while True:
        try:
            guessed_number = int(input("Enter you guessed Number :"))
            attempt += 1

            if guessed_number < winnng_number:
                print("The Number you guessed is too low! Try Again.")
            elif guessed_number > winnng_number:
                print("The Number you guessed is too high! Try Again.")
            else:
                print(f"Congratulations! You guesses the number {winnng_number} in {attempt} attempts.")
        except ValueError:
            print("Please Enter a valid number.")


number_guessing_game()