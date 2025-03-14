# Create a list to store inputted numbers
numbers = []

while True:
    # Ask user to input a number
    user_input = input("Enter a number: ")

    try:
        # Convert the input to a float and add to the list
        user_number = float(user_input)
        numbers.append(user_number)
    except ValueError:
        
        # Check if the input is valid or invalid
        if len(numbers) > 0:
            # Sort the list in ascending order
            numbers.sort()
            
            # Print all the numbers added to in the list
            print("Numbers from lowest to highest are:")
            for num in numbers:
                print(num)
        else:
            
            # If no valid numbers were entered
            print("No valid numbers were entered.")
        
        # Exit the loop when invalid input
        break