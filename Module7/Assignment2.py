name = input("")
names = set()
while name != (""):
    if names.__contains__(name):
        print("Existing name")
    else:
        names.update({name})
        print("New name")
    name = input("")
print(names)