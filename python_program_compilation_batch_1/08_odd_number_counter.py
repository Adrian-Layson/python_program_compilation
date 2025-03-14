# set the odd counter to 0
odd_count = 0

# ask for 10 inputs
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))   
    if number % 2 != 0: # check if number is odd
        odd_count += 1 # if odd, add one to odd counter

# print the total odd numbers
print(f"The total count of odd numbers are : {odd_count}")