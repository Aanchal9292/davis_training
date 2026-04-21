# Function to assign grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'Fail'

toppers = []        # List to store topper names
highest = 0         # Variable to track highest marks

try:
    # Open file in read mode
    with open("studentresult.txt", "r") as file:
        for line in file:
            try:
                # Remove newline and split by comma
                data = line.strip().split(",")

                # Extract student details
                sid = data[0]
                name = data[1]

                # Convert marks to integers
                m1 = int(data[2])
                m2 = int(data[3])
                m3 = int(data[4])

                # Calculate total and percentage
                total = m1 + m2 + m3
                percentage = total / 3

                # Get grade
                grade = calculate_grade(percentage)

                # Display result
                print(f"{name} -> Total: {total}, %: {percentage:.2f}, Grade: {grade}")

                # Check for topper
                if total > highest:
                    highest = total
                    toppers = [name]   # New topper list
                elif total == highest:
                    toppers.append(name)  # Multiple toppers

            except (ValueError, IndexError):
                # Handles invalid data (missing or wrong format)
                print("Invalid record skipped:", line)

    print("\nTopper(s):", toppers)

except FileNotFoundError:
    # Handles file not found error
    print("File not found!")