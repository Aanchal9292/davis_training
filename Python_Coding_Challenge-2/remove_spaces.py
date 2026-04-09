# Function to remove spaces from string
def remove_spaces(text):
    result = ""
    for ch in text:
        if ch != " ":
            result += ch
    return result

text = input("Enter string: ")
print(remove_spaces(text))