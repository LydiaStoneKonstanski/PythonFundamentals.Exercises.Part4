#I wrote fizzbuzz from memory in a new language in the allergist's office this morning.
#Crying for joy, or maybe because of all these 2am bedtimes!

def fizz_buzz() -> None:
    '''The program prints each number from 1 to 100 to a new line.
    If the num is multiple of three and five, prints "Fizz Buzz", if
    multiple of three prints "Fizz", an if multiple of five prints "Buzz".'''
    for num in range(101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizz_buzz()

