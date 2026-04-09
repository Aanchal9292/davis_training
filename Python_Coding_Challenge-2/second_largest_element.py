# Function to find second largest
def second_largest(nums):
    nums.sort()
    return nums[-2]

print(second_largest([10,20,5,15]))