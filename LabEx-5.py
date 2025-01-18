# Lab Exercises - 5
# Write a program that implements a user defined function that accepts Principal Amount, Rate, Time, Number of Times the interest is compounded to 
# calculate and displays compound interest. (Hint: CI=P*(1+r/n)nt)

def calculate_compound_interest(principal, rate, time, n):
    """
    Calculate compound interest.

    Parameters:
    principal (float): The principal amount (initial investment).
    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested or borrowed for (in years).
    n (int): The number of times that interest is compounded per year.

    Returns:
    float: The calculated compound interest.
    """
    # Convert rate from percentage to decimal
    r = rate / 100
    
    # Calculate compound interest
    compound_interest = principal * (1 + r/n)**(n*time)
    
    return compound_interest

def main():
    # Input from user
    principal = float(input("Enter the Principal Amount: "))
    rate = float(input("Enter the Rate of Interest (in %): "))
    time = float(input("Enter the Time (in years): "))
    n = int(input("Enter the Number of Times Interest is Compounded per Year: "))
    
    # Calculate Compound Interest
    total_amount = calculate_compound_interest(principal, rate, time, n)
    
    # Displaying the result
    print(f"The total amount after {time} years is: {total_amount:.2f}")
    
# Run the program
if __name__ == "__main__":
    main()
