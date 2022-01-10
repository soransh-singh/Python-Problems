"""
In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues.
The game offers one of the following hints in response to your guess:
    - “Pico” when your guess has a correct digit in the wrong place,
    - “Fermi” when your guess has a correct digit in the correct place,
    - “Bagels” if your guess has no correct digits.
You have 10 tries to guess the secret number.

# Take a random number
save them in a tuple
"""
import random

def main():
    number = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
    hundredth, tenth, ones = number
    print("{}{}{}".format(hundredth, tenth, ones))
    pass

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
