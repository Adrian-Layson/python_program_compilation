# make a variable with 0 value where we will be adding the even numbers
even_count = 0

# make a function with a range of 10 
for i in range(10):
    numbers = int(input(f"Enter the {i + 1} number: ")) # input 10 numbers
    if numbers % 2 == 0: # check if numbers are even
        even_count += 1 # add a count to our variable for every even number

# print the result
print(f"There are {even_count} even number: ")