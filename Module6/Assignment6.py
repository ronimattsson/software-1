import math

def calculate_unit_price(diameter, price):
    return price / (math.pi * (diameter/100/2)*(diameter/100/2))

diameter1 = int(input("Enter the diameter of the first pizza (cm): "))
price1 = int(input("Enter the price of the first pizza (euros): "))

diameter2 = int(input("Enter the diameter of the second pizza (cm): "))
price2 = int(input("Enter the price of the second pizza (euros): "))

unit1 = calculate_unit_price(diameter1, price1)
unit2 = calculate_unit_price(diameter2, price2)

print(f"Unit price of the first pizza: {unit1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit2:.2f} euros/m²")

if unit1 < unit2:
    winner = "first"
else:
    winner = "second"

print("The " + winner + " pizza provides better value for money.")