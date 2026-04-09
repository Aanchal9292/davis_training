# function for rotating list
def  rotate_list(nums):
    return [nums[-1]]+ nums[:-1]
print(rotate_list([1,2,3]))