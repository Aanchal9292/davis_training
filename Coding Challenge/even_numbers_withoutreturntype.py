def even_numbers(n):
    print("Even numbers are:")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=" ")

n = int(input("Enter N: "))
even_numbers(n)