unique_logs = set()   # Set to store unique ERROR logs

# Open log file
with open("log.txt", "r") as file:
    for line in file:
        # Check if line contains ERROR
        if "ERROR" in line:
            # Add to set (automatically removes duplicates)
            unique_logs.add(line.strip())

# Count unique error logs
error_count = len(unique_logs)

# Display logs
print("Unique ERROR logs:")
for log in unique_logs:
    print(log)

# Display total count
print("Total ERROR logs:", error_count)