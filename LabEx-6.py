# Lab Exercises - 6
# Write a program that has a user defined function to accept 2 numbers as parameters, if number 1 is less than number 2 then numbers are swapped and returned, i.e., 
# number 2 is returned in place of number1 and number 1 is reformed in place of number 2, otherwise the same order is returned.


def swap_if_less(num1, num2):
    """
    Swap two numbers if the first number is less than the second.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.

    Returns:
    tuple: A tuple containing the two numbers in the appropriate order.
    """
    if num1 < num2:
        return num2, num1  # Swap if num1 is less than num2
    else:
        return num1, num2  # Return in original order

def main():
    # Input from user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the swap function
    swapped_numbers = swap_if_less(number1, number2)
    
    # Displaying the result
    print(f"The numbers in the appropriate order are: {swapped_numbers[0]} and {swapped_numbers[1]}")

# Run the program
if __name__ == "__main__":
    main()
