import math


def calculate_standard_deviation():
    """
    Calculates the standard deviation of numbers entered by the user.
    Input stops when a negative number is entered.
    """
    numbers = []  # List to store all valid numbers
    sum_of_numbers = 0
    count = 0

    print("--- Standard Deviation Calculator ---")
    print("Enter positive numbers or 0. Enter a negative number to stop.")

    # 1. Input Loop and Appending to List
    while True:
        try:
            user_input = float(input("Enter a number: "))

            # Check for the stop condition
            if user_input < 0:
                break

            # Process valid input (positive or zero)
            numbers.append(user_input)
            sum_of_numbers += user_input
            count += 1

        except ValueError:
            # Handle cases where the user enters non-numeric text
            print("Invalid input. Please enter a number.")
            continue

    # 2. Handle Empty List (Reflection Question #3 Solution)
    if count == 0:
        print("\nError: No positive numbers or zero were entered. Cannot calculate standard deviation.")
        return

    # 3. Find the Mean (Loop)
    # The sum is already calculated, but we'll demonstrate a loop for educational purposes
    # sum_check = 0
    # for num in numbers:
    #     sum_check += num

    mean = sum_of_numbers / count

    # 4. Find the Numerator of the Standard Deviation (Loop)
    # The numerator is the sum of the squared differences: (x_i - mean)^2
    sum_of_squared_differences = 0

    for x_i in numbers:
        difference = x_i - mean
        squared_difference = difference ** 2
        sum_of_squared_differences += squared_difference

    # 5. Calculate the Final Standard Deviation
    # Variance = Numerator / N
    variance = sum_of_squared_differences / count

    # Standard Deviation = sqrt(Variance)
    standard_deviation = math.sqrt(variance)

    # 6. Report the result
    print("\n--- Calculation Results ---")
    print(f"Numbers entered: {numbers}")
    print(f"Total count (N): {count}")
    print(f"The mean (x-bar) is: {mean:.4f}")
    print(f"The standard deviation is: {standard_deviation}...")


# Run the program
calculate_standard_deviation()