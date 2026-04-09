# Function to convert string to uppercase
def to_upper(text):
    result = ""
    for ch in text:
        result += chr(ord(ch) - 32)
    return result

text = input("Enter string: ")
print(to_upper(text))