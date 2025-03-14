# make a variable with a value of 0 which where we will start
current_number = 0

# initialize a while loop that runs until the number is greater than 100
while current_number <= 100:
    if current_number % 10 != 0 and current_number % 10 != 5: # check if the number is not divisible by 10 and 5
        print(current_number) # print the current value of number if it doesn't meet the condition
    current_number += 1 # Increment the number