import numpy as np

# Input from user
num = int(input("Enter a number: "))

even_factors = []

# Finding factors
for i in range(1, num + 1):
    if num % i == 0:      # check factor
        if i % 2 == 0:    # check even
            even_factors.append(i)

# Creating NumPy array
arr = np.array(even_factors)

# Output
print("Even factors:", even_factors)
print("NumPy Array:", arr)