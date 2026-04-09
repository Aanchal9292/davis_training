# Function to classify age
def classify_age(age):
    if age < 18:
        return "Minor"
    elif age <60:
        return "Adult"
    else:
        return "Senior"
# Taking age from the user 
age = int(input("Enter the age : "))
print(classify_age(age))

