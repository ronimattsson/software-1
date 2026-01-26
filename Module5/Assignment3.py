integer = int(input("Enter an integer: "))
isPrime = 1
for i in range(2, integer//2+1):
    if integer % i == 0:
        isPrime = 0
        break
if isPrime and integer != 0 and integer != 1:
    print(str(integer) + " is a prime number.")
else:
    print(str(integer) + " is not a prime number.")
