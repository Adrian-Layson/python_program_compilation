# make a list where we will store the inputs
numbers = []
# ask user for 10 inputs
for i in range(10):
    num = float(input(f"Enter your {i + 1} number: "))
    numbers.append(num)
# display all the numbers, but only show the first entry of duplicates
print("Numbers: ")
seen = set() # use seen to track the numbersss that are already displayed

for num in numbers:
    if num not in seen:
        print(num)
        seen.add(num)