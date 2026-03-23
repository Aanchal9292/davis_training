# Set = unordered collection of UNIQUE elements
# No duplicates, no indexing, very fast lookup

fruits = {"apple", "banana", "mango", "apple"}
print(fruits)   # {"apple", "banana", "mango"} — duplicate removed!

# ── CREATE ──
empty_set = set()          # NOT {} — that creates dict!
from_list = set([1,2,2,3,3,3])  # {1, 2, 3}

# ── MODIFY ──
fruits.add("grape")        # add one item
fruits.update(["kiwi","pear"])  # add multiple
fruits.remove("banana")    # remove (raises error if not found)
fruits.discard("mango")    # remove (no error if not found)
fruits.pop()               # remove random item
fruits.clear()             # empty the set

# ── SET OPERATIONS (VERY USEFUL!) ──
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)       # Union:        {1,2,3,4,5,6,7}
print(a & b)       # Intersection: {3,4,5}
print(a - b)       # Difference:   {1,2} (in a but not b)
print(b - a)       # Difference:   {6,7} (in b but not a)
print(a ^ b)       # Symmetric:    {1,2,6,7} (not in both)

print(a.issubset({1,2,3,4,5,6}))   # True (a ⊆ bigger)
print(a.issuperset({1,2}))         # True (a ⊇ smaller)
print(a.isdisjoint({8,9,10}))      # True (no common elements)

# ── REAL USE CASE: Find common/unique items ──
students_py   = {"Aanchal", "Rahul", "Priya", "Ankit"}
students_java = {"Priya", "Ankit", "Suman", "Rohit"}

both    = students_py & students_java   # in both courses
only_py = students_py - students_java   # only in Python
either  = students_py | students_java   # in any course

print("Both:", both)       # {'Priya', 'Ankit'}
print("Only Python:", only_py)  # {'Aanchal', 'Rahul'}

# methods
# add
s = {1, 2, 3}
s.add(4)
print(s)

# update 
s.update([4, 5, 6])
print(s)

# remove
s.remove(2)
print(s)

# discard
s.discard(4)
print(s)

# pop
s.pop()
print(s)

# clear
s.clear()
print(s)

# union
a = {1, 2}
b = {3, 4}
print(a.union(b))

# intersection
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))

# difference
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))

# issubset
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))