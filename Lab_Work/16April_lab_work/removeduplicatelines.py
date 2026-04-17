seen = set()  # Set to store unique lines

# Open input and output files
with open("input.txt", "r") as f1, open("output.txt", "w") as f2:
    for line in f1:
        # Check if line already exists
        if line not in seen:
            f2.write(line)     # Write unique line
            seen.add(line)     # Add to set

print("Duplicates removed")