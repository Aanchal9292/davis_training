# Function to merge dictionaries
def merge_dict(a,b):

    a.update(b)

    return a

print(merge_dict({"a":1},{"b":2}))