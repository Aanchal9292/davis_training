list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]

# Validation
if not isinstance(list1, list) or not isinstance(list2, list):
    print("Inputs must be lists")
else:
    result_list = []

    for element in list1:
        if element not in list2:
            result_list.append(element)

    print("Result:", result_list)