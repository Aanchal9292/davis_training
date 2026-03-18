def even_numbers(n):
    evens = []
    for i in range(1, n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens

n = int(input("Enter N: "))
result = even_numbers(n)

print("Even numbers:", result)