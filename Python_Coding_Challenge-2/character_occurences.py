# Function to count occurrences of a character
def char_count(text, char):
    count = 0
    for ch in text:
        if ch == char:
            count += 1
    return count

print(char_count("banana", "a"))