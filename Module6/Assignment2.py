import random

def roll_dice(max):
    dice = random.randint(1, max)
    return dice


max = int(input("Please enter the max value: "))
while True:
    number = roll_dice(max)
    print(number)
    if number == max:
        break