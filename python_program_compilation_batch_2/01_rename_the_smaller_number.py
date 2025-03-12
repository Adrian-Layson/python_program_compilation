# ask user for two inputs
input_first_number = int(input("Enter your first number: "))
input_second_number = int(input("Enter your second number: "))
# compare the two inputs
if input_first_number > input_second_number:
   # print the smaller number
    print(f"The smaller number is: {input_second_number}")
else:
    print(f"The smaller number is: {input_first_number}")
