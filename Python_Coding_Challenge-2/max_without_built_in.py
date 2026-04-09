# Function to find maximum element
def max_value(nums):
    max_num = nums[0]

    for i in nums:
        if i > max_num:
            max_num = i

    return max_num

nums = [5,8,2]
print(max_value(nums))