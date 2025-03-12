# make a variable with a value of 0 which where we will start
number = 0
# initialize a while loop that runs until the number is greater than 100
while number <= 100:
    # check if the number is not divisible by 10 and 5
    if number % 10 != 0 and number % 10 != 5:
        # print the current value of number if it doesn't meet the condition
        print(number)
    # print the current value of number if it doesn't meet the condition
    number += 1