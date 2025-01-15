# Lab Exercises - 2
# Write a program that uses a user defined function that accepts name and gender (as M for Male, F for Female) and prefixes Mr/Ms on the basis of the gender.


def prefix_name(name, gender):
    """
    Prefix the name with Mr. or Ms. based on the gender.

    Parameters:
    name (str): The name to be prefixed.
    gender (str): The gender ('M' for Male, 'F' for Female).

    Returns:
    str: The prefixed name.
    """
    if gender.upper() == 'M':
        return f"Mr. {name}"
    elif gender.upper() == 'F':
        return f"Ms. {name}"
    else:
        return "Invalid gender input. Please use 'M' for Male or 'F' for Female."

# User input
name_input = input("Enter your name: ")
gender_input = input("Enter your gender (M/F): ")

# Get the prefixed name
result = prefix_name(name_input, gender_input)

# Display the result
print(result)
