def get_season(month):
    winter = [12,1,2]
    spring = [3,4,5]
    summer = [6,7,8]
    #autumn = [9,10,11]

    if winter.__contains__(month):
        return "winter"
    elif spring.__contains__(month):
        return "spring"
    elif summer.__contains__(month):
        return "summer"
    else:
        return "autumn"

month = int(input("Enter the number of a month (1-12): "))
print("You entered: " + str(month))
if month > 0 and month <= 12:
    print("The season is " + get_season(month) + ".")
else:
    print("Please enter a number between 1 and 12.")