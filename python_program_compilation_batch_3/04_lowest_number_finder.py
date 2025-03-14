# Create a list to store inputs
numbers = []

while True:
    #Ask user for input
    user_input = input("Enter a number: ")

    #Checks if input is a valid number
    try:
        user_number = float(user_input) # Checks if input is a valid number
        numbers.append(user_number) # Adds valid number to the list
    except ValueError:
        if len(numbers) > 0:
            print(f"The lowest number inputted is: {min(numbers)}") # Prints the lowest number inputted
        else:
            print("No valid numbers were entered.")
        break