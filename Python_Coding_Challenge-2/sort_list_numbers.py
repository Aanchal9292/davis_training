# function for sorting
def sort_list(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j] :
                nums[i] , nums[j] = nums[j] , nums[i]
    return nums
print(sort_list([3,1,2]))