input_tuple = (1, 2, 3, 4, 5)
target_sum = 5

pairs_list = []

# Validation
if isinstance(input_tuple, tuple):

    for i in range(len(input_tuple)):
        for j in range(i + 1, len(input_tuple)):

            if input_tuple[i] + input_tuple[j] == target_sum:
                pairs_list.append((input_tuple[i], input_tuple[j]))

    print("Pairs:", pairs_list)

else:
    print("Input must be tuple")