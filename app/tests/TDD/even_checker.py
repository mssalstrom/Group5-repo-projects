# Function to check if a given number is even
def is_even(number):
    # Check if the input is a number (integer or float)
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number")
    # Return True if the number is even, False otherwise
    return number % 2 == 0
