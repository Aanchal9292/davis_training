# Create a list of 15 numbers
numbers = [5, 8, 3, 8, 12, 7, 8, 20, 15, 8, 9, 1, 8, 14, 6]

print("Original List:", numbers)

# Take input from user
num = int(input("Enter a number to search: "))

# Check if number exists in the list
if num in numbers:
    first_index = numbers.index(num)   # Find first occurrence

    # Remove all other occurrences
    i = first_index + 1
    while i < len(numbers):
        if numbers[i] == num:
            numbers.pop(i)
        else:
            i += 1

    print("Updated List:", numbers)
else:
    print("Number not found in the list.")