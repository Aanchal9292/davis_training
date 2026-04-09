# Function to print multiplication table
def table(n):
    for i in range(1, 11):
        print(n*i, end=" ")

n = int(input("Enter the number : "))
table(n)