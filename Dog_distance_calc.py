speed=int(input("How fast did Brutus run?   "))
time=int(input("How many hours did Brutus play?   "))

print("Hour \t Brutus' Distance")
print("-" * 35)

for hour in range (1, time+1):
    distance=(speed*hour)
    print(hour, "\t", distance, "km")