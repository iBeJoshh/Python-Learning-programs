#Joshua Adkins #tip calculator #1/24/2023

#asks for the price of the food and drinks
food = float(input("What is the price of food and drinks?: "))

tip = food * 0.2

#calculates tax total
tax = food * 0.065

#calculates the total between the tax + food
total = food + tax + tip

#print command for users
print("Subtotal: $",round(food,2))
print("Tax: $",round(tax,2))
print("Tip: $",round(tip,2))
print("Total: $",round(total,2))

print(input('\n\nHit Enter to Close\n'))