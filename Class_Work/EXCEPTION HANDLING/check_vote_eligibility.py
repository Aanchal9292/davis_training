# Program to check voting eligibility using exception handling

try:
    # Taking input from user
    age = int(input("Enter your age: "))
    
    print("-----------------------")
    print("Checking voting eligibility for age:", age)
    
    # Checking eligibility
    if age >= 18:
        print("You are eligible to vote.")
    elif age > 0:
        print("You are not eligible to vote.")
    else:
        print("Invalid age entered!")
    
    print("-----------------------")

# Handles wrong input like string
except ValueError:
    print("Please enter a valid number")

# (Optional) Handles unexpected type errors
except TypeError:
    print("Unexpected data type")

# Executes if no exception occurs
else:
    print("----------------------")
    print("Program executed successfully")

# Always executes
finally:
    print("Program Executed")