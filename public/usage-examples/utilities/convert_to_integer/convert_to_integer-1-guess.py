from splashkit import *

write_line("Welcome to the Number Guessing Game!")
write_line("I'm thinking of a number between 1 and 100...")

# Set a secret number
secret_number = 42

guess = -1  # Initialise with an invalid guess

# Ask the user for their guess
while guess != secret_number:
    write_line("Please enter your guess:")
    input_value = read_line()

    # Validate if the input is a valid integer
    if is_integer(input_value):
        # Convert input string to integer
        guess = convert_to_integer(input_value)

        # Check if the guess is correct
        if guess == secret_number:
            write_line(f"Congratulations! You've guessed the correct number: {guess}")
        elif guess < secret_number:
            write_line("Too low! Try again.")
        else:
            write_line("Too high! Try again.")
    else:
        write_line("That's not a valid integer! Please enter a number.")