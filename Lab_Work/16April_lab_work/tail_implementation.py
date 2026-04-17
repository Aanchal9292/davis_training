# Take number of lines from user
n = int(input("Enter number of lines: "))

# Read file
with open("file.txt", "r") as f:
    lines = f.readlines()

# Print last n lines
for line in lines[-n:]:
    print(line.strip())