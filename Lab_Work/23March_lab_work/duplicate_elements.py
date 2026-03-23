# Input list
number_list = [1, 2, 3, 2, 4, 5, 1]

# Validation
if not isinstance(number_list, list):
    print("Invalid input. Must be a list")
else:
    seen_elements = []
    duplicate_elements = []

    for number in number_list:
        if number in seen_elements and number not in duplicate_elements:
            duplicate_elements.append(number)
        else:
            seen_elements.append(number)

    print("Duplicate elements:", duplicate_elements)