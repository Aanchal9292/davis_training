# funtion to calculate  simple interest
def calculatesi(p,r,t):
    return ((p*r*t)/100)
#---------------
# main program
principal = float(input("Enter the principal(in Rs.) : "))
rate = float(input("Enter the rate of interest(in %) : "))
time = float(input("Enter the time(in years) : "))
print("Simple Interest : ",calculatesi(principal,rate,time))