# Set the total to 0
total = 0

# Ask for 10 inputs
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))

# Add all the numbers inputted 
    total += number

# Print the sum
print(f"The sum of all numbers is : {total}")