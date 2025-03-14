# ask user for two inputs
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

# compare the two inputs
if first_number > second_number:
   
   # print the smaller number
    print(f"The smaller number is: {second_number}")
elif first_number < second_number:
    print(f"The smaller number is: {first_number}")
else:
    print("Both numbers are equal")

