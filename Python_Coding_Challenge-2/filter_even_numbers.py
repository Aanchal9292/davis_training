# Function to print even numbers
def even_numbers(n):
    for i in range(2, n+1, 2):
        print(i, end=" ")

n = int(input())
even_numbers(n)