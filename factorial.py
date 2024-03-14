"""
Given a number (x), determine the value of x!
Use recursion
x		result
0!		1
1!	1 * 1	1
2!	2 * 1	2
3!	3 * 2 * 1	6
4!	4 * 3 * 2 * 1	24
5!	5 * 3 * 2 * 1	120
...	...	...
Constraints

n >= 0 n < 995
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def print_factorial(n):
    if n >= 0 and n < 995:
        print(factorial(n))
    else:
        print("number is out of range")

print_factorial(7)





