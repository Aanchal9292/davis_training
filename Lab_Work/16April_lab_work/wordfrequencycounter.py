import string  # Used to remove punctuation

freq = {}  # Dictionary to store word count

# Open file
with open("article.txt", "r") as f:
    for line in f:
        # Convert to lowercase (ignore case)
        line = line.lower()
        
        # Remove punctuation marks
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Split into words
        words = line.split()

        # Count frequency of each word
        for word in words:
            freq[word] = freq.get(word, 0) + 1

# Print result
for word, count in freq.items():
    print(word, ":", count)