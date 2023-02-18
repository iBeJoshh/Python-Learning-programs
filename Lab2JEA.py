#Joshua Adkins    #Lab 2      #2/12/2023  #Amusement park admission calc



height = float(input("Enter Height of the Guest: "))

if height < 30:
    teir_name = "Guppy"
    cost = 0
elif height < 36:
    teir_name = "Pollywog"
    cost = 2
elif height < 42:
    teir_name = "Apprentice"
    cost = 5
elif height < 48:
    teir_name = "Explorer"
    cost = 8
else:
    teir_name = "Adventurer"
    cost = 10

print("Guest Teir Is:",teir_name)
print("The cost of the ticket is: $" + str(cost))