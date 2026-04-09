# function for checking divisibility
def check_divisibility(num):
    if (num%5 ==0 & num%3 ==0):
        return "Yes"
    else :
        return "No"
# taking input from user
num = int(input("Enter the number : "))
print(check_divisibility(num))
    