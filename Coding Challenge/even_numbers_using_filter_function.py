n = int(input("Enter N: "))

even = list(filter(lambda x: x%2==0, range(1,n+1)))

print(even)