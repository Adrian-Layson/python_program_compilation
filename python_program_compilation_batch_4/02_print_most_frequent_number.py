# create a list to store inputs
numbers = []

# ask user for input until invalid
while True:
    try:
        number = int(input("Please input a number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input, stopping.")
        break

# find the most frequent number
if numbers:
    most_frequent = max(set(numbers), key=numbers.count)
    count = numbers.count(most_frequent)
    print(f"Most frequent number is: {most_frequent}, appearing {count} times.")