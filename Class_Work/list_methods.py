# ── CREATE ──
nums    = [1, 2, 3, 4, 5]
mixed   = [1, "hello", 3.14, True, None]
nested  = [[1,2,3], [4,5,6], [7,8,9]]
empty   = []

# ── ACCESS ──
print(nums[0])          # 1 (first)
print(nums[-1])         # 5 (last)
print(nums[1:4])        # [2, 3, 4]
print(nums[::2])        # [1, 3, 5] (every 2nd)
print(nums[::-1])       # [5, 4, 3, 2, 1] (reversed)
print(nested[1][2])     # 6

# ── MODIFY ──
nums[0] = 100
nums.append(6)          # add to end: [100,2,3,4,5,6]
nums.insert(1, 999)     # insert at index 1
nums.extend([7,8,9])    # add multiple items
nums.remove(100)        # remove first occurrence of 100
nums.pop()              # remove & return last item
nums.pop(0)             # remove & return at index 0
del nums[0]             # delete at index

# ── SEARCH ──
print(3 in nums)         # True
print(nums.index(3))     # position of 3
print(nums.count(3))     # how many times 3 appears

# ── SORT ──
nums.sort()              # ascending in-place
nums.sort(reverse=True)  # descending in-place
sorted_nums = sorted(nums) # returns new sorted list
nums.reverse()           # reverse in-place

# ── COPY ──
a = [1, 2, 3]
b = a          # b is SAME list (alias!)
c = a.copy()   # c is a NEW independent copy
d = a[:]       # also a copy (slicing)
e = list(a)    # also a copy

# ── LIST COMPREHENSION ── (VERY IMPORTANT!)
squares  = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

evens    = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

words    = ["hello", "world", "python"]
upper    = [w.upper() for w in words]
# ["HELLO", "WORLD", "PYTHON"]

matrix   = [[i*j for j in range(1,4)] for i in range(1,4)]
# [[1,2,3],[2,4,6],[3,6,9]]

# conditional expression in comprehension
labels = ["even" if x%2==0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# ── USEFUL FUNCTIONS ──
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(nums))        # 8
print(sum(nums))        # 31
print(max(nums))        # 9
print(min(nums))        # 1
print(sorted(nums))     # [1,1,2,3,4,5,6,9]