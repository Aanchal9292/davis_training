# function for even or odd
def evenodd(x):
  if x%2 == 0:
    print("Even")
  else:
    print("Odd")
# main program
num = int(input("Enter the number : "))
print(evenodd(num))