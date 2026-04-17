# Open both input files and output file
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f3:
    
    # Combine lines of both files
    lines = f1.readlines() + f2.readlines()

    # Add line numbers while writing
    for i, line in enumerate(lines, start=1):
        f3.write(f"{i}. {line}")

print("Files merged with line numbers")