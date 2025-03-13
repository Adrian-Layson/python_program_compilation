# create a list to store inputs
numbers = []

while True:
    #ask user for input
    user_input = input("Enter a number: ")

    #checks if input is a valid number
    try:
        number = float(user_input) # checks if input is a valid number
        numbers.append(number) # adds valid number to the list
    except ValueError:
        if len(numbers) > 0:
            print(f"The lowest number inputted is: {min(numbers)}") # prints the lowest number inputted
        else:
            print("No valid numbers were entered.")
        break