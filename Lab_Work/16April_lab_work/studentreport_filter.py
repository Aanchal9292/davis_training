# Open input file and output file
with open("students.txt", "r") as f1, open("filtered.txt", "w") as f2:
    
    # Read file line by line
    for line in f1:
        # Split data into name, marks, city
        name, marks, city = line.strip().split(",")
        
        # Check condition for marks
        if int(marks) > 75:
            # Write qualifying record into new file
            f2.write(line)

print("Filtered data saved")