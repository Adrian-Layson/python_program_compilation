# ask two inputs from user
input_first_number = int(input("Enter your first number: "))
input_second_number = int(input("Enter your second number: "))

# compare the two inputs
if input_first_number > input_second_number:
    print(f"The larger number is: {input_first_number} ") # find the larger number and print
elif input_first_number < input_second_number:
    print(f"The larger number is: {input_second_number}")
else:
    print("Both numbers are equal")