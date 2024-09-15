import random


def guessing_game():
    # Computer draws a random number between 1 and 10
    number_to_guess = random.randint(1, 10)

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        user_input = input("Enter your guess: ")

        try:
            guess = int(user_input)  # Convert input to integer

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Correct! You guessed the number.")
                break  # Exit the loop when the guess is correct
        except ValueError:
            print("Please enter a valid integer.")


# Run the game
guessing_game()
