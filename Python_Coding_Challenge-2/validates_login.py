# Function to validate login
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Login"

user = input("Enter username: ")
pwd = input("Enter password: ")

print(login(user, pwd))