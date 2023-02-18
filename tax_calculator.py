#Joshua Adkins #Sales tax calculator #1/24/2023

#Asks for the sales tax for location
tax = float(input("What is the sales tax rate?: "))

#asks for the price of each item
item1_total = float(input("What is the price of item #1?: "))
item2_total = float(input("What is the price of item #2?: "))
item3_total = float(input("What is the price of item #3?: "))

#adds together all 3 items
subtotal = item1_total + item2_total + item3_total

#calculates tax total
tax = subtotal * tax

#calculates the total between the tax + items
total = subtotal + tax

#print command for users
print("Subtotal: $",round(subtotal,2))
print("Tax: $",round(tax,2))
print("Total: $",round(total,2))

print(input('\n\nHit Enter to Close\n'))