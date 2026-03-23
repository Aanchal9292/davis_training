set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Validation
if isinstance(set1, set) and isinstance(set2, set):

    intersection_result = set1.intersection(set2)
    difference_result = set1.difference(set2)

    print("Intersection:", intersection_result)
    print("Difference:", difference_result)

else:
    print("Inputs must be sets")