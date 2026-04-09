# Function to count vowels in a string
def count_vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1
    return count

text = input("Enter string: ")
print(count_vowels(text))