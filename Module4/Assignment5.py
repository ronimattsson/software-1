username = "python"
password = "rules"
i = 0
while i < 5:
    input_user = input("Enter username: ")
    input_pass = input("Enter password: ")
    if input_user == username and input_pass == password:
        print("Welcome")
        break
    else:
        if (i != 4):
            print("Incorrect username or password. Please try again.")
        else:
            print("Access denied")
    i+=1
