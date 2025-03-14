# ask user for two numbers
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

# check if the first number is greater than the second number, swap if first number is greater than second number
if first_number > second_number:
    first_number, second_number = second_number, first_number

# for loop all the numbers between the first and second number, excluding both
for result in range(first_number +1, second_number):
    # print the result
    print(result)
    