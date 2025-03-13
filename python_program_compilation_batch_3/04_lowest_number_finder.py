# create a list to store inputs
numbers = []

while True:
    # ask user for input
    user_input = input("Enter a number: ")

    # check if the input is a valid number
    if user_input.replace('-', '', 1).isdigit() or (user_input[0] == '-' and user_input[1:].replace('.', '', 1).isdigit()):
        numbers.append(int(user_input)) # store the number as an integer
    else:
    # if input is not valid, exit the loop and show the lowest number
        if len(numbers) > 0:
            print(f"The lowest number inputted is: {min(numbers)} ")
        else:
            print("No valid numbers were entered.")
        break