# Open both files
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    
    # Convert lines into sets
    lines1 = set(f1.readlines())
    lines2 = set(f2.readlines())

# Find difference
difference = lines1 - lines2

# Display result
print("Lines in file1 but not in file2:")
for line in difference:
    print(line.strip())