# create a list to store inputs
numbers = []

# ask user for input until invalid
while True:
    try:
        number = int(input("Please input a number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input, stopping.")
        break
    
# find the most frequent number