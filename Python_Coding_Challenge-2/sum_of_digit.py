# Function to calculate sum of digits
def sum_digits(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total

num = int(input())
print(sum_digits(num))