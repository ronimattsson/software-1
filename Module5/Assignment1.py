import random

dice = input("How many dice to roll: ")
sum = 0
for i in range(int(dice)):
    sum += random.randint(1,6)
print("Sum of the dice: " + str(sum))