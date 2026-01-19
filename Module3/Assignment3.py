gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
if gender != "male" and gender != "female":
    print("Invalid gender.")
else:
    if (hemoglobin < 134 and gender == "male") or (hemoglobin < 117 and gender == "female"):
        print("Your hemoglobin is low.")
    elif (hemoglobin > 167 and gender == "male") or (hemoglobin > 155 and gender == "female"):
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is normal.")