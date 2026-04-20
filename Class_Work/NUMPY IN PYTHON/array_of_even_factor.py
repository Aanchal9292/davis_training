import numpy as np

# Input
num = int(input("Enter a number: "))

# Conditions
if num == 0:
    print("Zero does not have finite factors. Please enter a non-zero number.")

elif num < 0:
    print("Negative numbers are not allowed. Please enter a positive number.")

elif num % 2 != 0:
    print("The number is odd, so it has no even factors.")

else:
    even_factors = []

    # Finding factors
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            even_factors.append(i)

    # Creating NumPy array
    arr = np.array(even_factors)

    # Output
    print("Even factors:", even_factors)
    print("NumPy Array:", arr)