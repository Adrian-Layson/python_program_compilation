# Input the first number
first_number = int(input("Enter the first number: "))

# Give the value of the first number to a variable
result = first_number

# Make a function with a range of 9 since we already have the first number
for i in range(9):
    number = int(input(f"Enter your {i + 2} number: ")) # Input the remaining numbers
    result -= number # Substract to the first number

# Print the result
print(result)