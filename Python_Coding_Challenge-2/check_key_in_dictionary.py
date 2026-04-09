# Function to check key
def check_key(d, key):

    if key in d:
        return "Yes"
    else:
        return "No"

print(check_key({"a":1,"b":2},"a"))