import random

def roll_dice():
    dice = random.randint(1, 6)
    return dice

while True:
    number = roll_dice()
    print(number)
    if number == 6:
        break