# Function to count digits
def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num //= 10

    return count

num = int(input())
print(count_digits(num))