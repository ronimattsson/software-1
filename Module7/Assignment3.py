def ask_for_option():
    return int(input("\nAirport Data Management\n"
          "1. Enter a new airport\n"
          "2. Fetch airport information\n"
          "3. Quit\n"
          "Please choose an option (1-3): "))

option = ask_for_option()
airports = {}
while option != 3:
    if option == 1:
        code = input("Enter the ICAO code: ")
        airport = input("Enter the airport name: ")
        if airport not in airports:
            airports.update({code: airport})
            print("Airport " + airport + " with ICAO code " + code + " has been added.")
        else:
            print("Airport with ICAO code " + code + " already exists.")
    elif option == 2:
        code = input("Enter the ICAO code: ")
        if code in airports:
            print("The airport with ICAO code " + code + " is " + airports[code] + ".")
        else:
            print("No airport found with ICAO code " + code + ".")
    elif option != 3:
        print("Please enter a valid option.")
    option = ask_for_option()
print("Thank you for using the Airport Data Management system. Goodbye!")