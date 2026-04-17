# Program to calculate area and circumference of a circle
# using exception handling

import math   # Importing math module to use pi value

try:
    # Taking input from user
    radius = float(input("Enter the radius of the circle: "))
    
    # Checking if radius is negative
    if radius < 0:
        raise ValueError("Radius cannot be negative!")
    
    # Calculating area
    area = math.pi * radius * radius
    
    # Calculating circumference
    circumference = 2 * math.pi * radius
    
    # Displaying results
    print("Area of circle is:", area)
    print("Circumference of circle is:", circumference)

# Handling error if user enters non-numeric value
except ValueError as ve:
    print("Error:", ve)

# Handling any other unexpected errors
except Exception as e:
    print("Something went wrong:", e)

# This block always executes
finally:
    print("Program executed successfully (with or without errors).")