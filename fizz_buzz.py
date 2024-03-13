def fizz_buzz():
    for num in range(100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            continue
        elif num % 3 == 0:
            print("Fizz")
            continue
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizz_buzz()
#The program prints each number from 1 to 100 to a new line.
#If the number is a multiple of 3, print "Fizz" instead of the number.
#If the number is a multiple of 5, print "Buzz" instead of the number.
#If the number is a multiple of both 3 and 5, print "FizzBuzz" instead of the number.
