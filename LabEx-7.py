# Lab Exercises - 7
# Write a program that contains user defined functions to calculate area, perimeter or surface area whichever is applicable for various shapes like square, 
# rectangle, triangle, circle and cylinder. The user defined functions should accept the values for calculation as parameters and the calculated value should be returned. 
# Import the module and use the appropriate functions.


import math

def area_square(side):
    """Calculate the area of a square."""
    return side ** 2

def perimeter_square(side):
    """Calculate the perimeter of a square."""
    return 4 * side

def area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def perimeter_rectangle(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)

def area_triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def perimeter_triangle(side1, side2, side3):
    """Calculate the perimeter of a triangle."""
    return side1 + side2 + side3

def area_circle(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def circumference_circle(radius):
    """Calculate the circumference of a circle."""
    return 2 * math.pi * radius

def surface_area_cylinder(radius, height):
    """Calculate the surface area of a cylinder."""
    return 2 * math.pi * radius * (radius + height)

def volume_cylinder(radius, height):
    """Calculate the volume of a cylinder."""
    return math.pi * radius ** 2 * height

def main():
    print("Choose a shape to calculate:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Cylinder")
    
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        side = float(input("Enter the side length of the square: "))
        print(f"Area: {area_square(side)}")
        print(f"Perimeter: {perimeter_square(side)}")
        
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"Area: {area_rectangle(length, width)}")
        print(f"Perimeter: {perimeter_rectangle(length, width)}")
        
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        side1 = float(input("Enter side 1 length: "))
        side2 = float(input("Enter side 2 length: "))
        side3 = float(input("Enter side 3 length: "))
        print(f"Area: {area_triangle(base, height)}")
        print(f"Perimeter: {perimeter_triangle(side1, side2, side3)}")

    elif choice == 4:
        radius = float(input("Enter the radius of the circle: "))
        print(f"Area: {area_circle(radius)}")
        print(f"Circumference: {circumference_circle(radius)}")

    elif choice == 5:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        print(f"Surface Area: {surface_area_cylinder(radius, height)}")
        print(f"Volume: {volume_cylinder(radius, height)}")

    else:
        print("Invalid choice! Please select a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
