# Function to check prime number
def is_prime(n):

    for i in range(2,n):
        if n % i == 0:
            return "Not Prime"

    return "Prime"

print(is_prime(7))