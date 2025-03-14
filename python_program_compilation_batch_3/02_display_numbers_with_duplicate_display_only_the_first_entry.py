# Make a list where we will store the inputs
numbers = []

# Ask user for 10 inputs
for i in range(10):
    num = float(input(f"Enter your {i + 1} number: "))
    numbers.append(num)

# Display all the numbers, but only show the first entry of duplicates
print("Numbers: ")
seen_numbers = set() # Use seen to track the numbers that are already displayed

for num in numbers:
    if num not in seen_numbers:
        print(num)
        seen_numbers.add(num)