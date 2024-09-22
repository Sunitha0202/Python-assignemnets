import random

# Function that returns a random dice roll between 1 and 6
def roll_dice():
    return random.randint(1, 6)

# Main program to roll dice until the result is 6
def main():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print(f"Rolled: {roll}")

# Call the main function
main()