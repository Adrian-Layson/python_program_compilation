# Create an empty list to store user inputs
numbers = []

while True:
    try:
        # Ask user to input a number
        user_input = float(input("Enter a number: "))
# Check if the numbe has a duplicate
        if numbers.count(user_input) == 0:
            print("Unique")
        else:
            print("duplicate")
# Add the number to the list for future comparison
        numbers.append(user_input)

    except ValueError:
# If user enters a non-numerical input, exit the loop
        print("Invalid input. Exiting the program.")
        break
