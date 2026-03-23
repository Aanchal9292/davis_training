set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Validation
if isinstance(set1, set) and isinstance(set2, set):

    result_set = set1.symmetric_difference(set2)

    print("Symmetric Difference:", result_set)

else:
    print("Inputs must be sets")