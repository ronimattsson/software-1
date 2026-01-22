numberList = []
while True:
    number = input("Enter a number: ")
    if str(number) == "":
        break
    elif len(numberList) < 5:
        numberList.append(int(number))
    else:
        numberList.sort()
        if numberList[0] < int(number):
            numberList[0] = int(number)
numberList.sort(reverse=True)
print("The greatest numbers in descending order:")
for i in numberList:
    print(f"{i:.1f}")