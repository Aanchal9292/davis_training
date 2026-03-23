nested_list = [[1, 2], [3, 4], [5]]

# Validation
if isinstance(nested_list, list):

    # Using list comprehension
    flat_list = [element for sublist in nested_list for element in sublist]

    print("Flattened List:", flat_list)

else:
    print("Input must be a list")