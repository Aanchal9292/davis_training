# Program for writing data into a file
# Opening file for write operation
filev = open("firstfile.txt", "w")
# blank list of sentences
sentences = []
# Writing five sentences into the file
print("Enter any 5 sentences:")

for x in range(5):
    # Input of data from user
    sentence = input()
    
    # inserting the sentence into the list
    sentences.append(sentence)
    print("--------------------")
# -----------------------------
# writing data into the file
filev.writeLines(sentences)
print("Data successfully written!")

# Closing the file
filev.close()