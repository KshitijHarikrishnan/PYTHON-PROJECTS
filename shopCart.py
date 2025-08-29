#SHOPPING CART PROGRAM & 2D LIST(NUM PAD)
num_pad = ((1, 2, 3),
           (4, 5, 6),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()    


foods = []
prices = []
total = 0

while True:
    food = input("Enter a food item (q to exit): ")
    if food.lower() == "q":
        break
    price = float(input("Enter price of item: $"))
    foods.append(food)
    prices.append(price)

print("ITEMS IN CART :")

for food in foods:
    print(food, end = "\n")

for price in prices:
    total = float(sum(prices))
    
print()
print(f"The total cost of the items is ${total}")     


