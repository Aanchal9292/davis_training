# Program for writing data into a file
# Opening file for write operation
filev = open("firstfile.txt", "w")

# Writing five sentences into the file
print("Enter any 5 sentences:")

for x in range(5):
    # Input of data from user
    sentence = input(f"Sentence {x+1}: ")
    
    # Writing sentence into the file
    # We add + "\n" to ensure each sentence starts on a new line
    filev.write(sentence + "\n")
    print("--------------------")

print("Data successfully written!")

# Closing the file
filev.close()