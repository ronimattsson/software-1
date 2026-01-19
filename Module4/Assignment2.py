while True:
    inch = float(input("Enter length in inches (negative value to quit): "))
    if inch < 0:
        break
    else:
        centimeter = inch * 2.54
        print(f"{inch:.1f} inches is {centimeter:.2f} centimeters")
print("Program ended.")