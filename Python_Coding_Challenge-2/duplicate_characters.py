# Function to find duplicate characters
def duplicate_chars(text):
    seen = set()
    dup = set()

    for ch in text:
        if ch in seen:
            dup.add(ch)
        else:
            seen.add(ch)

    return dup

print(duplicate_chars("programming"))