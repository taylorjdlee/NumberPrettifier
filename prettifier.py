# Function to prettify numbers
def number_prettifier(num):
    # If the number is negative it cannot be to prettified
    if num < 0:
        return "Negative number cannot be prettified"
    # Return the value as a string as it's under a million
    elif num < 1_000_000:
        return str(num)
    # Format a value within the millions
    elif 1_000_000 <= num < 1_000_000_000:
        return number_to_string(num, 1_000_000, "M")
    # Format a value within the billions
    elif 1_000_000_000 <= num < 1_000_000_000_000:
        return number_to_string(num, 1_000_000_000, "B")
    # Format a value within the trillions
    elif 1_000_000_000_000 <= num < 1_000_000_000_000_000:
        return number_to_string(num, 1_000_000_000_000, "T")
    # If the number is quadrillion or more it's too large to prettify
    else:
        return "Number too large to prettify"
    
# Function to produces a prettified string version of a number
# It takes the num, divisor, and unit as input to cut down on reused code
def number_to_string(num, divisor, unit):
    result = num / divisor
    # If statement to check if the result is an integer or float
    if num % divisor == 0:
        return f"{int(result)}{unit}"
    else:
        return f"{result:.1f}{unit}"