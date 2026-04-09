# Function to check number type
def number_type(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

num = int(input("Enter the number : "))
print(number_type(num))