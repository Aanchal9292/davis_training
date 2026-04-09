# Function to count words
def word_count(sentence):
    words = sentence.split()
    return len(words)

sentence = input()
print(word_count(sentence))