# Read all lines from file
with open("input.txt", "r") as f1:
    lines = f1.readlines()

# Write lines in reverse order
with open("reverse.txt", "w") as f2:
    for line in reversed(lines):
        f2.write(line)

print("File reversed")