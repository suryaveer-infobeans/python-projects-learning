import random


def number_guessing_game():
    secret_number = random.randint(1,100)
    guess = None

    print('Welcome to the Number Guessing Game!')
    print('I,m thinking of a number between 1 and 100')
    print('Can you guess what it is?')

    while guess != secret_number:
        guess = int(input('Enter your guess'))

        if guess < secret_number:
            print('Too low! Try Again')
        elif guess > secret_number:
            print('Too High! Try Again')
        else:
            print('Congratulations! You guess the correct Number')

number_guessing_game()