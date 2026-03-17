# to find out factorial of a number
num = int(input("Enter a number :"))
if(num<0):
  print("Not possible")
elif(num==0):
  print("Factorial is 1")
else:
  fact = 1
  for x in range(1,num+1):
    fact = fact*x
  print("Factorial : ",fact)