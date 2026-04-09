# Function to replace vowels
def replace_vowels(text):
    result = ""
    for ch in text:
        if ch in "aeiouAEIOU":
            result += "*"
        else:
            result += ch
    return result

text = input("Enter string: ")
print(replace_vowels(text))