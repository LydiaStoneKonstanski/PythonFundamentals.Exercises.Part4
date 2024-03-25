
from random import randrange

#Helper Functions

current_guess = 0
def first_number_guess_prompt() -> None:
    '''A function that asks the user to provide a number between 0 and 10 to initiate game.'''
    global current_guess
    user_guess = int(input('Can you guess my number between 1 and 10?\n'))
    current_guess = user_guess
    return current_guess


def random_number_generator() -> int:
    '''function to generate and return a number'''
    return randrange(1,11)


def number_comparison(random_number, current_guess) ->bool:
    '''function to compare number to guess and provide feedback'''
    if random_number > current_guess:
        print(str(current_guess) + ' was too low!\n')
    elif random_number < current_guess:
        print(str(current_guess) + ' was too high!\n')
    elif random_number == current_guess:
        print('My number was ' + str(random_number) + '. ' + str(current_guess) + ' was correct!\n')
        return True
    return False

#function to prompt a new guess
def new_guess_prompt() ->int:
    new_guess = int(input('Guess again between 1 and 10!\n'))
    return new_guess


def main():
    '''Main function calls the helpers in order'''
    global current_guess
    first_number_guess_prompt()
    random_number = random_number_generator()

    while True:
        if number_comparison(random_number, current_guess):
            break
        current_guess = new_guess_prompt()


main()