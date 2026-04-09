# Function to sort dictionary
def sort_dict(d):

    for k in sorted(d):
        print(k,":",d[k])

sort_dict({"b":2,"a":1})