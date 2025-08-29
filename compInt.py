#COMPOUND INTEREST CALCULATOR
import math
principal = 0
rate = 0 
time = 0
amount = 0

#while True loop will continue forever. We'll need to break it explicitly
while True:
    principal = float(input("Enter the principal: $"))
    if principal <= 0:
        print("Principal has to be > 0")
    else:
        break    

while True:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("rate has to be > 0")     
    else:
        break

while True:
    time = int(input("Enter the time: "))
    if principal <= 0:
        print("time has to be > 0")
    else:
        break            

 

amount = principal * pow(1 + rate/100, time)
print(amount)