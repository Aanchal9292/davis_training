input_list = [1, 2, 2, 3, 4, 4]

# Validation
if isinstance(input_list, list):

    # Using set() to remove duplicates
    result_tuple = tuple(set(input_list))

    print("Result:", result_tuple)

else:
    print("Input must be a list")