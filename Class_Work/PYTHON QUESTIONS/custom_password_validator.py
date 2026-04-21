# 4. Custom Password Validator
# Rules:
# • Min 8 chars
# • At least 1 uppercase, 1 lowercase, 1 digit
# Use:
# • string operations
# • loops + conditionals
# • Raise custom exception if invalid 

# Custom exception class
class InvalidPassword(Exception):
    pass

# Function to validate password
def validate_password(password):

    # Check minimum length
    if len(password) < 8:
        raise InvalidPassword("Password too short")

    # Check for uppercase letter
    if not any(c.isupper() for c in password):
        raise InvalidPassword("Must contain uppercase letter")

    # Check for lowercase letter
    if not any(c.islower() for c in password):
        raise InvalidPassword("Must contain lowercase letter")

    # Check for digit
    if not any(c.isdigit() for c in password):
        raise InvalidPassword("Must contain a digit")
    
    # Check for character@#$%^&
    special_ch = "!@#$%^&*()"
    if not any(c in special_ch for c in password):
        raise InvalidPassword("Must contain a special character")
    

    return True

try:
    pwd = input("Enter password: ")

    # Validate password
    validate_password(pwd)

    print("Valid Password")

except InvalidPassword as e:
    # Handle custom exception
    print("Error:", e)