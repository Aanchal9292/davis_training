# Function to find largest number
def largest(a, b, c):
    max_num = a

    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c

    return max_num

a = int(input())
b = int(input())
c = int(input())

print(largest(a, b, c))