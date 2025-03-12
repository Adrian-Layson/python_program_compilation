# set the total to 0
total = 0
# ask for 10 inputs
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
# add all the numbers inputted 
    total += number
# print the sum
print(f"The sum of all numbers is : {total}")