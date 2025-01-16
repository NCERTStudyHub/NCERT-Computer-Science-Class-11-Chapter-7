# Lab Exercises - 3
# Write a program that has a user defined function to accept the coefficients of a quadratic equation in variables and calculates its determinant. 
# For example : if the coefficients are stored in the variables a,b,c then calculate determinant as b2-4ac. Write the appropriate condition to check 
# determinants on positive, zero and negative and output appropriate result


def calculate_determinant(a, b, c):
    """Calculate the determinant of a quadratic equation."""
    return b**2 - 4*a*c

def main():
    # Accepting coefficients from the user
    try:
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))
        
        # Ensure 'a' is not zero for a valid quadratic equation
        if a == 0:
            print("Coefficient 'a' cannot be zero for a quadratic equation.")
            return
        
        # Calculate the determinant
        determinant = calculate_determinant(a, b, c)
        
        # Check the value of the determinant and output the result
        if determinant > 0:
            print("The determinant is positive. The quadratic equation has two distinct real roots.")
        elif determinant == 0:
            print("The determinant is zero. The quadratic equation has exactly one real root (repeated).")
        else:
            print("The determinant is negative. The quadratic equation has no real roots (two complex roots).")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for coefficients.")

# Run the main function
if __name__ == "__main__":
    main()
