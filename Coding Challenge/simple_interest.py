def simpleinterest(principle,rate,time):
    si = (principle*rate*time)/100
    return si

# taking principle from user
principle = float(input("Enter the principle (in Rs.) : "))
# taking rate from user
rate = float(input("Enter the rate (in %) : "))
# taking time from user
time = float(input("Enter the time (in years) : "))
si = simpleinterest(principle,rate,time)
print("Simple Interest : Rs. ",si)