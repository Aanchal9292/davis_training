keys_tuple = ('a', 'b', 'c')
values_tuple = (1, 2, 3)

# Validation
if isinstance(keys_tuple, tuple) and isinstance(values_tuple, tuple):

    if len(keys_tuple) == len(values_tuple):

        # Using zip() and dict()
        result_dictionary = dict(zip(keys_tuple, values_tuple))

        print("Dictionary:", result_dictionary)

    else:
        print("Tuples must have equal length")

else:
    print("Inputs must be tuples")