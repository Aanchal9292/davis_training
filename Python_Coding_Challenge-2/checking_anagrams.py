# Function to check anagram
def is_anagram(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

a = input("Enter first word : ")
b = input("Enter second word : ")

print(is_anagram(a, b))