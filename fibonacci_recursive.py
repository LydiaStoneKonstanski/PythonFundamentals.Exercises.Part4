#Given a term (n), determine the value of x(n).
#create a function called fibonnaci. The function should take in an integer and return the value of x(n).
def fibonnaci(num):
        if num == 1:
            return 0
        elif num == 2:
            return 1
        else:
            return fibonnaci(num-1) + fibonnaci(num-2)
#Constraint
for i in range(1, 31):
    print(fibonnaci(i))