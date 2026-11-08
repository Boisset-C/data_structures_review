# DATA STRUCTURES AND ALGORITHM PATTERNS

# 1. Foundations

# ARRAYS: default data structure for most things if its linear and ordered it is probably stored as an array
#  - numbers
#  - chars
#  - objects

array = ["A", "C", "H", "K"]

# linear and ordered
# access: O(1)
# append: O(1)
# insert/delete: O(n)

# lookup is constant time
array[4] = "K" # O(1)

# insert something at the beginning
array.append("J") # amortized O(1) or O(n) if capacity ran out and memory allocation needs to happen

# to delete
array.pop() # O(1) if empty it returns an IndexError

# USECASE: When to use arrays? How well can you leverage?
# - Traverse a structure in order
# - Access specific indices
# - Compare elements from both ends
# - Sliding window, prefix sum, etc

#-------------------------------------------------------------------------------------------------------

# STRINGS: are immutable, making a change builds a new one. Besides that they work mostly like arrays.

# DON'T DO -- >common mistake: creates a new string with every change on iteration.

text = "Some text"

results = ""
for char in text:
    results += char

# INSTEAD DO: build an array and then join it. 
result = []

def build_string(text):
  for char in text:
      result.append(char)

  return "".join(result) # O(n)

# USECASE: often hidden as sliding window problems or two pointers
# - Find the longest substring without repeating characters
# - Check if two strings are anagrams
# - Return all substrings that match a pattern

#-------------------------------------------------------------------------------------------------------

# SET: a collection of unique values. given a list of numbers and need to check for a certain number, you can # check in O(1) time on average.

# Example:

nums = [1, 2, 3, 4, 5]
seen = set(nums) # O(1) faster than looping through things
print( 3 in seen)  

# USECASE: used for tracking
# - Uniqueness
# - Existence
# - Fast membership checks
# - Sliding window

# NOT for storing key/value pairs 

#-------------------------------------------------------------------------------------------------------

# CONTROL FLOW & LOOPING: Most interview problems boiling down to three things
# - A loop
# - Some conditions
# - A few variables being updated

# KNOW LIKE BACK OF HAND: walk through code with a sample input
n = 1
for i in range(n):
   pass

arr = []
for val in arr:
   pass

start = 0
end = 10
while start < end:
   pass

# if, else, elif
# break, continue

#-------------------------------------------------------------------------------------------------------

# EFFICIENCY Big O Notation

# Worse Case (top) --> Best Case (Bottom)
# O(n!): Factorial time
# O(2^n): Exponential time
# O(n^2): Quadriatic time
# O(n): linear time
# O(log n): logarithmic time
# O(1): constant time <-- Best Case







