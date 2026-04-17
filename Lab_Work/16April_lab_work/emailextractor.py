import re  # Regular expression module

# Read full file content
with open("data.txt", "r") as f:
    content = f.read()

# Find all email patterns
emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', content)

# Write emails into new file
with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

print("Emails extracted")