list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [2, 5, 3]

# Validation
if isinstance(list1, list) and isinstance(list2, list) and isinstance(list3, list):

    common_elements = list(set(list1).intersection(list2, list3))

    print("Common Elements:", common_elements)

else:
    print("All inputs must be lists")