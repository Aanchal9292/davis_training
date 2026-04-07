# function to check number is even or odd
def evenodd(n):
    if(n%2==0):
        return "even"
    else: 
        return "odd"
# main program
num = int(input("Enter the number : "))
print("Given number is ",evenodd(num))

