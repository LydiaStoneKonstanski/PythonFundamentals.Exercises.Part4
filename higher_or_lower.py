#A function that asks the user to provide a number between 0 and 10.
from random import randrange

#Helper Functions

current_guess = 0
#function to intitiate game
def first_number_guess_prompt():
    global current_guess
    user_guess = int(input('Can you guess my number between 1 and 10?\n'))
    current_guess = user_guess
    return current_guess

#function to generate and return a number
def random_number_generator():
    return randrange(1,11)

#function to compare number to guess and provide feedback
def number_comparison(random_number, current_guess):
    if random_number > current_guess:
        print(str(current_guess) + ' was too low!\n')
    elif random_number < current_guess:
        print(str(current_guess) + ' was too high!\n')
    elif random_number == current_guess:
        print('My number was ' + str(random_number) + '. ' + str(current_guess) + ' was correct!\n')
        return True
    return False

#function to prompt a new guess
def new_guess_prompt():
    new_guess = int(input('Guess again between 1 and 10!\n'))
    return new_guess



#Main function calls the helpers in order
def main():
    global current_guess
    first_number_guess_prompt()
    random_number = random_number_generator()

    while True:
        if number_comparison(random_number, current_guess):
            break
        current_guess = new_guess_prompt()

#calls main to run the program
main()