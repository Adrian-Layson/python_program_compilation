# Set the odd counter to 0
odd_count = 0

# Ask for 10 inputs
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))   
    if number % 2 != 0: # Check if number is odd
        odd_count += 1 # If odd, add one to odd counter

# Print the total odd numbers
print(f"The total count of odd numbers are : {odd_count}")