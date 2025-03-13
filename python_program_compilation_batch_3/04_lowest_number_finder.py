# create a list to store inputs
numbers = []

while True:
    # ask user for input
    user_input = input("Enter a number: ")

# check if the input is a valid number
    if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
        numbers.append(int(user_input)) # store the number as an integer

# if input is not valid, exit the loop and show the lowest number