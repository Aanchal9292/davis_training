# Function to count numbers > 50
def count_greater(nums):
    count = 0
    for i in nums:
        if i > 50:
            count += 1
    return count

nums = [10,60,30,80]
print(count_greater(nums))