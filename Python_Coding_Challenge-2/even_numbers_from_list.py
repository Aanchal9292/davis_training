# Function to return even numbers
def even_numbers(lst):

    result = []

    for i in lst:
        if i % 2 == 0:
            result.append(i)

    return result

print(even_numbers([1,2,3,4]))