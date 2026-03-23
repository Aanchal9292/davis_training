list_of_sets = [{1, 2}, set(), {3, 4}, set()]

# Validation
if isinstance(list_of_sets, list):

    # Using list comprehension
    result_list = [s for s in list_of_sets if len(s) > 0]

    print("Result:", result_list)

else:
    print("Input must be a list")