# Function to find common elements
def common_elements(a, b):
    result = []

    for i in a:
        if i in b:
            result.append(i)

    return result

print(common_elements([1,2,3],[2,3,4]))