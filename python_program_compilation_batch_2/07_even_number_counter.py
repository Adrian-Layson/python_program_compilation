# Make a variable with 0 value where we will be adding the even numbers
even_count = 0

# Make a function with a range of 10 
for i in range(10):
    numbers = int(input(f"Enter the {i + 1} number: ")) # Input 10 numbers
    if numbers % 2 == 0: # Check if numbers are even
        even_count += 1 # Add a count to our variable for every even number

# Print the result
print(f"There are {even_count} even number: ")