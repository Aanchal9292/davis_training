# Function to check palindrome string
def is_palindrome(s):
    if s == s[::-1]:
        return "Yes"
    else:
        return "No"

s = input("Enter string: ")
print(is_palindrome(s))