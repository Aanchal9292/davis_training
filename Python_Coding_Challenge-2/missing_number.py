# Function to find missing number
def missing_number(nums):

    for i in range(1,6):
        if i not in nums:
            return i

print(missing_number([1,2,4,5]))