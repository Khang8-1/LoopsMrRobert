# Program #1: Counting

# Initialize variables
count_positive = 0
count_negative = 0
sum_of_numbers = 0
total_numbers_for_average = 0

while True:
    try:
        # Read an integer from the user
        user_input = int(input("Please enter an integer: "))

        # Check for the loop termination condition
        if user_input == 0:
            break  # Exit the loop if the input is 0

        # Process the non-zero input
        if user_input > 0:
            count_positive += 1
        else: # user_input < 0
            count_negative += 1

        # Update sum and count for the average calculation
        sum_of_numbers += user_input
        total_numbers_for_average += 1

    except ValueError:
        # Basic error handling for non-integer input
        print("Invalid input. Please enter a whole number.")
        continue # Skip the rest of the loop and ask for input again

# Output the results
print("You entered", count_positive, "positive numbers.")
print("You entered", count_negative, "negative numbers.")

# Calculate and report the average, handling the case of no valid input
if total_numbers_for_average > 0:
    average = sum_of_numbers / total_numbers_for_average
    print(f"The average of your numbers is {average}")
else:
    print("No numbers were entered besides the terminating 0, so the average cannot be calculated.")