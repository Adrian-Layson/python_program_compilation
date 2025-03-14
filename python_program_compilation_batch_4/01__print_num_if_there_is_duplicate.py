# create an empty list
numbers = []

# ask user for input
for i in range(10):  
    num = int(input(f"Enter your {i + 1} number: "))
    numbers.append(num) # add the inputs to the list numbers

# print the numbers that have duplicates
print("Numbers that have duplicates: ")

# loop through each number in the list, and if the count of the number is greater than 1, print the number.
for num in set(numbers):  
    if numbers.count(num) > 1:  
        print(num)