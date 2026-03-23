input_tuple = (5, 1, 8, 3)

# Validation
if isinstance(input_tuple, tuple):

    # Using built-in methods
    max_value = max(input_tuple)
    min_value = min(input_tuple)

    print("Max =", max_value)
    print("Min =", min_value)

else:
    print("Input must be tuple")