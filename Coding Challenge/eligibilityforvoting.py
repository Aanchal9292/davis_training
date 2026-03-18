# taking age as input
age = int(input("Enter the age : "))
if (0<age<18):
    print("You are not eligible for voting !!")
elif(age<0):
    print("Provide valid age ")
else:
    print("You are eligible for voting !!")