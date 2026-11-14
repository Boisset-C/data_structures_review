# TWO POINTERS
#  Foundational pattern for linear structures:
# - arrays
# - strings
# - linked lists

# THE KEY: is to recognize when to use it. You use two indices or pointers to move through a structure, usually in a way that helps avoid nested loops or repeated scanning. 

# "Linear" means elements sit in a sequence you walk in order.
# It does NOT mean sorted. Sorting only matters for some opposite-direction problems.

# TWO MAJOR TYPES

# TYPE 1 SAME DIRECTION (both start at or near the beginning): 
# a) Fast / Slow (speeds differ: fast moves 2, slow moves 1)
#    - fast reaches the end -> slow is at the middle
#    - fast laps slow -> cycle detected (mainly linked lists)
# b) Read / Write (in-place edits on arrays)
#    - read pointer visits every elements
#    - write pointer only visits every element
#    - usecase: removing duplicates, moving zeros
# c) Two sequences (one pointer per sequence)
#    - e.g. merging two sorted arrays
# Note: sorting only required for c) which relies on being sorted

# MENTAL MODEL: SAME DIRECTION
# 1. both start at 0 (or slow = 0, fast = 1)
# 2. fast/read pointer advances everystep
# 3. slow/write pointer advances only when a condition is met (or at half speed)

# TYPE 2 OPPOSITE DIRECTIONS (start at both ends, meet in the middle):
#   - sorted array: find a pair/combination hitting a target (REQUIRES SORTED)
#   - symmetry checks like palindrome (does NOT require sorted, compares equality)
#   - avoiding nested loops when examining pairs

# MENTAL MODEL: OPPOSITE DIRECTION
# 1. left = 0, right = last index
# 2. check the current pair agaisnt the condition
# 3. move one pointer inward based on the result
# 4. stop when they meet (or the condition is satisfied)

# Why it works on sorted input: each comparison rules out a whole row/column of pairs
# so O(n) instead of O(n^2)

# WHEN TO USE TWO POINTERS
# - fewer iterations: O(n) instead of O(n^2)
# - tracks a relationship between two positions
# - O(1) extra space: no set or map needed (the advantage over hashing)

# TRADEOFF vs HASH MAP (unsorted Two Sum):
# - hash map: O(n) time, O(n) space
# - sort + two pointers: O(n log n) time, loses original indices
# - two pointers wins when input is already sorted or O(1) space is required


# PROBLEMS WHERE TWO POINTERS COME UP (scanning two pairs?)
# - Palindromes
# - Reversals 
# - Merging sorted data
# - "K" sized comparisons


def is_palindrome(s: str):
  l, r = 0, len(s) - 1

  while l < r:
    while l < r and not s[l].isalnum():
      l += 1
    while l < r and not s[r].isalnum():
      r -= 1
    if s[l].lower() != s[r].lower():
      return False
    l += 1
    r -= 1
  return True


number = 121



# if with digits we can very fast solve a palindrome using
# when way I can still optimize is check even/odd and see if at the middle I can check for 
# palindrome
def is_num_palindrome(x):
  current = x
  remainder = 0
  potential_palindrome = 0

  while current > 0:
    remainder = current % 10
    current = current // 10

    potential_palindrome = (potential_palindrome * 10) + remainder

  return potential_palindrome == x


  # middle of a linked list
  def find_middle(list):
    slow = fast = end

    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next

    return slow.next
  

  