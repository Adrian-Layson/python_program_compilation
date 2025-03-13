# create an empty list to store user inputs
numbers = []

while True:
    try:
        # ask user to input a number
        num = float(input("Enter a number: "))
# check if the numbe has a duplicate
        if numbers.count(num) == 0:
            print("Unique")
        else:
            print("duplicate")
# add the number to the list for future comparison
        numbers.append(num)

except ValueError:
# if user enters a non-numerical input, exit the loop
        print("Invalid input")
        break
