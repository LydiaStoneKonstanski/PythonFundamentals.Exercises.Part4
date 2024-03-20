#I wrote fizzbuzz from memory in a new language in the allergist's office this morning.
#Crying for joy, or maybe because of all these 2am bedtimes!

def fizz_buzz():
    for num in range(100): #The program prints each number from 1 to 100 to a new line.
        if num % 3 == 0 and num % 5 == 0: #If the number is a multiple of both 3 and 5, print "FizzBuzz" instead of the number.
            print("FizzBuzz")
            #continue
        elif num % 3 == 0: #If the number is a multiple of 3, print "Fizz" instead of the number.
            print("Fizz")
            #continue
        elif num % 5 == 0: #If the number is a multiple of 5, print "Buzz" instead of the number.
            print("Buzz")
        else:
            print(num)


fizz_buzz()


# for i in range(1,101):
#     if i % 3 == 0 and i == 0:
#         print("FizzBuzz")
#     elif i % 3 === 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


