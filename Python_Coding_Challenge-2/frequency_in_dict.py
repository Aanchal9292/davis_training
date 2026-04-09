# Function to count frequency
def frequency(nums):

    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq

print(frequency([1,2,2,3]))