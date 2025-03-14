# Create an empty list
numbers = []

# Ask user for input
for i in range(10):  
    input_number = int(input(f"Enter your {i + 1} number: "))
    numbers.append(input_number) # add the inputs to the list numbers

# Print the numbers that have duplicates
print("Numbers that have duplicates: ")

# Loop through each number in the list, and if the count of the number is greater than 1, print the number.
for current_number in set(numbers):  
    if numbers.count(current_number) > 1:  
        print(current_number)