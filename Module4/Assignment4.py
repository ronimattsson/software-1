import random

randomnumber = random.randint(1,10)
while True:
    number = float(input("Guess a number: "))
    if number == randomnumber:
        print("Correct")
        break
    elif number < randomnumber:
        print("Too low")
    elif number > randomnumber:
        print("Too high")