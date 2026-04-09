# Function to check vowel
def is_vowel(ch):
    if ch in "aeiouAEIOU":
        return "Vowel"
    else:
        return "Not Vowel"

char = input("Enter character: ")
print(is_vowel(char))