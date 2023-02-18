#Joshua Adkins #Brownie recipe per 9 converter #1/24/2023
import math

cups_butter = 0.50
eggs = 2
vanilla_tbsp = 1
cup_sugar = 1
cup_flour = 0.50
cocoa_powder = 0.50
baking_powder_tsp = 0.25
salt_tsp = 0.25

#Ask user how many brownies they want
brownies = float(int(input("How many Brownies do you want to make?: ")))

#math to adjust for how many brownies they want
cups_butter *= brownies /9
eggs *= brownies /9
vanilla_tbsp *= brownies /9
cup_sugar *= brownies /9
cup_flour *= brownies /9
cocoa_powder *= brownies /9
baking_powder_tsp *= brownies /9
salt_tsp *= brownies /9

#Displays whats needed
print("Ingredients for", brownies, "brownies")
print("Cups of Butter:", cups_butter)
print("Eggs:", eggs)
print("Tablespoon of Vanilla:", vanilla_tbsp)
print("Cups of sugar:",cup_sugar)
print("Cups of flower:",cup_flour)
print("Cups of cocoa powder:",cocoa_powder)
print("Teaspoon of baking powder:",baking_powder_tsp)
print("Teaspoon of salt:",salt_tsp)