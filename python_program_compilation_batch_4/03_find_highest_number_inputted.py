# Create a list to store values
numbers = []

# Ask user for input until invalid
while True:
    number = input("Please input a number: ")
    if number.isdigit(): # checks if input is a digit
        numbers.append(int(number))
    else:
        print("Invalid input")
        break

# Check and print the highest number submitted
if numbers:
    print(f"The highest number inputted is: {max(numbers)}")