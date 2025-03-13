#  make a list to store the numbers that will be inputted
numbers = []
# ask user for 10 inputs
for i in range(10):
    num = int(input(f"Enter your {i + 1} number: "))
    numbers.append(num)
# display the numbers that don't have duplicates
print("Numbers that don't have duplicates: ")
# check each number in the list
for num in numbers:
    if numbers.count(num) == 1: # if the count of number is 1, it's unique
        print(num)