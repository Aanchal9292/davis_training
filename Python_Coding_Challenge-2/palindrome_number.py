# Function to check palindrome number
def palindrome(num):
    temp = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    if temp == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"

num = int(input())
print(palindrome(num))