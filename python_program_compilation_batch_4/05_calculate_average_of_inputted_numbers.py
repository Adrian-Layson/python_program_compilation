# list to store values
numbers = []

# ask user for input until invalid
while True:
    number = input("Please input a number: ")
    if number.isdigit():
        numbers.append(int(number))
    else:
        print("Invalid input")
        break

# calculate and display the average inputted numbers
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average inputted number is: {average}")
