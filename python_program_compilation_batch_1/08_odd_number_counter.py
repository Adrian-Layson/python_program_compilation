# set the odd counter to 0
odd_count = 0

# ask for 10 inputs
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    # check if number is odd   
    if number % 2 != 0:
    # if odd, add one to odd counter
        odd_count += 1

# print the total odd numbers
print(f"The total count of odd numbers are : {odd_count}")