shift = 3  # Number of positions to shift

# Open input and output file
with open("input.txt", "r") as f1, open("encrypted.txt", "w") as f2:
    
    for line in f1:
        encrypted = ""
        
        # Process each character
        for ch in line:
            if ch.isalpha():  # Check if alphabet
                # Handle uppercase and lowercase separately
                if ch.isupper():
                    encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
                else:
                    encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
            else:
                encrypted += ch  # Keep special characters unchanged
        
        # Write encrypted line
        f2.write(encrypted)

print("File encrypted")