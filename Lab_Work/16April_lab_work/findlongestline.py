max_line = ""      # Store longest line
max_length = 0     # Store maximum length

# Open file
with open("data.txt", "r") as f:
    for line in f:
        # Compare length of each line
        if len(line) > max_length:
            max_length = len(line)
            max_line = line

# Display result
print("Longest Line:", max_line)
print("Length:", max_length)