#FACTORIAL PROGRAM IN PYTHON

#1) ITERATIVE APPROACH:

def factorial(x):
    result = 1
    if x > 0:
        for y in range(1,x+1):
            result *= y

    print(result)

a = int(input("Enter a number > 0 for its factorial (ITERATIVE WAY): "))
factorial(a)

#2) RECURSIVE APPROACH:

def Factorial(x):
    
    if x == 1:
        return 1
    else:
        return x * Factorial(x-1)
    


b = int(input("Enter a number > 0 for its factorial (RECURSIVE WAY): "))
print(Factorial(b))