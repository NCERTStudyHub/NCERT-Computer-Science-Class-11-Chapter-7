# Lab Exercises - 1
# Write a program to check the divisibility of a number by 7 that is passed as a parameter to the user defined function.

def is_divisible_by_7(number):
    """
    Check if the given number is divisible by 7.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is divisible by 7, False otherwise.
    """
    return number % 7 == 0

# User input
try:
    user_input = int(input("Enter a number to check its divisibility by 7: "))
    
    # Check divisibility
    if is_divisible_by_7(user_input):
        print(f"{user_input} is divisible by 7.")
    else:
        print(f"{user_input} is not divisible by 7.")
except ValueError:
    print("Please enter a valid integer.")
