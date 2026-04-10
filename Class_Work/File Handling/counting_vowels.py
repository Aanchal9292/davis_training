# Program to count vowels in a file

# Open the file in read mode
file = open("firstfile.txt", "r")

# Read the content of the file
data = file.read()

# Initialize vowel count
vowel_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
for char in data:
    if char in vowels:
        vowel_count += 1

# Display result
print("Number of vowels in the file:", vowel_count)

# Close the file
file.close()