""" The following code includes a function that doubles a number provided by the user.

Module 1 Part 2 Homework
ATMS 523
Erin Welch
"""

def double_number(value):
    """Returns the given value multiplied by two.

    Args: 
        value (float) represents the number to double.
    
    Returns:
        (float): the doubled value.
    """
    return value * 2


def main():
    """Prints the double of a number provided by the user."""
    number = float(input("Enter a Number: "))
    result = double_number(number)
    print(f"Entered Value: {number}")
    print(f"Doubled Value: {result}")


if __name__ == "__main__":
    main()