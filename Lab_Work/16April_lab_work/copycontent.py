# Open source file in read mode and destination file in write mode
with open("source.txt", "r") as f1, open("destination.txt", "w") as f2:
    # Read entire content of source file
    data = f1.read()
    
    # Write content into destination file
    f2.write(data)

# Display success message
print("File copied successfully")