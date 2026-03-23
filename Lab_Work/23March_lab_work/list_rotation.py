# Input data
number_list = [10, 20, 30, 40, 50]
k = 2

# Validation
if not isinstance(number_list, list) or not isinstance(k, int):
    print("Invalid input")
else:
    length = len(number_list)
    k = k % length

    rotated_list = number_list[-k:] + number_list[:-k]

    print("Rotated List:", rotated_list)