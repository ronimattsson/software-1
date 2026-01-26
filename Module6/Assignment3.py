def gallons_to_liters(gallons):
    return float(gallons*3.785)

gallons = int(input("Enter a volume in American gallons (negative value to quit): "))
while gallons > 0:
    print(f"{gallons:.1f} American gallons is {gallons_to_liters(gallons):.2f} liters.")
    gallons = int(input("Enter a volume in American gallons (negative value to quit): "))
print("Program finished.")