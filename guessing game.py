import random


def guessing_game():
    """
    Simulates a number guessing game.
    The computer picks a random number (0-100), and the user tries to guess it.
    The program provides "Too high" or "Too low" clues.
    """

    # 1. Initialize the game state
    # Generate a random integer between 0 and 100 (inclusive)
    secret_number = random.randint(0, 100)

    # Initialize the guess counter
    guess_count = 0

    # Initialize the user's guess to a value outside the valid range to ensure the loop starts
    guess = -1

    # Print introductory message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 100.")

    # 2. Main game loop (Iteration/Looping)
    # The loop continues as long as the user has not guessed the secret number
    while guess != secret_number:
        try:
            # Get the user's input
            user_input = input("Enter your guess: ")

            # Convert the input to an integer
            guess = int(user_input)

            # Increment the guess counter
            guess_count += 1

            # 3. Selection Statement (Conditionals/If-Elif-Else)
            # Check the guess against the secret number and provide a clue
            if guess > secret_number:
                print("Too high")
            elif guess < secret_number:
                print("Too low")
            # If the guess is neither too high nor too low, it must be correct.
            # The loop condition (guess != secret_number) will handle the exit.

        except ValueError:
            # Handle non-integer input gracefully
            print("Invalid input. Please enter a whole number.")
            # Do not increment guess_count for invalid input
        except EOFError:
            # Handle sudden end of input
            print("\nGame aborted.")
            return

    # 4. Success message (runs only after the loop condition is met)
    print(f"\nYou got it! It took you {guess_count} guesses.")


# Start the game
if __name__ == "__main__":
    guessing_game()
