# input the first number
first_number = int(input("Enter the first number: "))
# give the value of the first number to a variable
result = first_number
# make a function with a range of 9 since we already have the first number
for i in range(9):
    # input the remaining numbers
    number = int(input(f"Enter your {i + 2} number: "))
    # substract to the first number
    result -= number
# print the result
print(result)