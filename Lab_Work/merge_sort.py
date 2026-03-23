list1 = [3, 1, 2]
list2 = [2, 4, 5]

# Validation
if isinstance(list1, list) and isinstance(list2, list):

    merged_list = list1 + list2

    unique_list = list(set(merged_list))

    # Using built-in sort()
    unique_list.sort()

    print("Result:", unique_list)

else:
    print("Inputs must be lists")