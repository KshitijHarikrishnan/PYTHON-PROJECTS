#CALCULATOR AND OTHERS
import math

#List = [] ordered and changeable
#Set = {} unordered and immutable, but can ADD/REMOVE element
#Tuple = () ordered and unchangeable.

'''
letter = ["A", "B", "C"]
#print(help(fruits))
letter.append("D")
letter.remove("C")
letter.insert(0,"Z")
letter.sort()
letter.reverse()
#letter.clear
print(letter.index('Z'))
print(letter)
'''

'''
fruits = {"apple", "banana", "coconut"}
fruits.add("pineapple")
fruits.remove("banana")
fruits.pop() #removes a random element from set
fruits.clear()
print(fruits)
'''

print("1", "2", "3", sep = " ") #sep is a keyword arg in print function to seperate values

num1 = int(input("Enter 1st number: "))
operator = input("Enter an operator (+, -, /, *): ")
num2 = int(input("Enter 2nd number: "))

if operator == '+':
    print(round(num1 + num2, 3))
elif operator == '-':
    print(round(num1 - num2, 3))
elif operator == '*':
    print(round(num1 * num2, 3))
elif operator == '/':
    print(round(num1 / num2, 3))
else:
    print(f"{operator} is not a valid operator")
    