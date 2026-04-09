# Function to find longest word
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for w in words:
        if len(w) > len(longest):
            longest = w

    return longest

sentence = input("Enter sentence: ")
print(longest_word(sentence))