# Create a list to store inputs
numbers = []

# Ask user for input until invalid
while True:
    number = input("Please input a number: ")
    if number.isdigit():
        numbers.append(int(number))
    else:
        print("Invalid input")
        break

# Sort numbers from highest to lowest and print
if numbers:
    numbers.sort(reverse=True)
    print(f"Numbers from highest to lowest: {numbers}")
