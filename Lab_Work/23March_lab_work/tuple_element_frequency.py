input_tuple = (1, 2, 2, 3, 1, 4)

# Validation
if isinstance(input_tuple, tuple):

    frequency_dictionary = {}

    for element in input_tuple:
        frequency_dictionary[element] = input_tuple.count(element)

    print("Frequency:", frequency_dictionary)

else:
    print("Input must be a tuple")