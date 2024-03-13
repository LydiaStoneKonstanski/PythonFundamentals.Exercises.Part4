# Given a term (n), determine the value of x(n).
# In the fibonacci_linear.py program, create a function called fibonnaci. The function should take in an integer and return the value of x(n).
# This problem must be solved WITHOUT the use of recursion.
# Constraints
# n >= 0


def fibonacci_linear(num):
    if(num == 0):
        return 0
    elif num == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, num + 1):
            c = a + b
            a = b
            b = c
        return c


for i in range(1, 31):
    print(fibonacci_linear(i))
