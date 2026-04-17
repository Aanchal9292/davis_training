# Take keyword input from user
keyword = input("Enter keyword: ")

# Open file
with open("file.txt", "r") as f:
    for line in f:
        # Case-insensitive search
        if keyword.lower() in line.lower():
            print(line.strip())  # Print matching line