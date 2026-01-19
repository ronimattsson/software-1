high = ""
low = ""
while True:
    number = input("Enter a number (or press Enter to quit): ")
    if number == "":
        break
    elif high == "":
        high = number
        low = number
    elif float(number) > float(high):
        high = number
    elif float(number) < float(low):
        low = number
print(f"Smallest number: {float(low):.1f}\n"
      f"Largest number: {float(high):.1f}")