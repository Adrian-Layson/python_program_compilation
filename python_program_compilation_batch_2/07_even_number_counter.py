# make a variable with 0 value where we will be adding the even numbers
even_count = 0
# make a function with a range of 10 
for i in range(10):
   # input 10 numbers
    numbers = int(input(f"Enter the {i + 1} number: "))
# check if numbers are even
    if numbers % 2 == 0:
        # add a count to our variable for every even number
        even_count += 1
# print the result
print(f"There are {even_count} even number: ")