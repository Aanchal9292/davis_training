set1 = {1, 2}
set2 = {1, 2, 3, 4}

# Validation
if isinstance(set1, set) and isinstance(set2, set):

    result = set1.issubset(set2)

    print(result)

else:
    print("Inputs must be sets")