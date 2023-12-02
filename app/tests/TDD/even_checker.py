
def is_even(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number")
    return number % 2 == 0
