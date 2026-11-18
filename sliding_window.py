from collections import defaultdict
from typing import List

# SLIDING WINDOW PROBLEM
# gives you a subset of data, never revisiting same element. Constrains context
# Reduce to O(n)

# Two Main types of sliding window problems:
# 1) Fixed Window: 
# Example: 
#  - Find the maximum avarage of any subarray of size k
#  - Return the sum of every k-length block. 
#  - Find the subarray of length k with the largest/smallest X.
# as you slide the window remove from the right and add from the left, updating results based # on current context: 

def sliding_window_fixed(input, window_size):
  # ans = window = input[0:window_size]
  # for right in range(window_size, len(input)):
  #  left = right - window_size
  #  remove input[left] from window
  #  append input[right] to window
  #  ans = optimal(ans, window)
  # return
  pass

# 2) Dynamic Window:
# Examples:
# Find the length of the longest substring with at most K unique characters
# What's the smallest subarray with a sum greater than a target
# Return the longest window where a certain rule is valid

# Core pattern:

def sliding_window_flexible_longest(input):
 # initialize window, ans
 # left = 0
 # for right in range(len(input)):
 #    append input[right] to window
 #    while invalid(window):
 #      remove input[left] from window
 #      left += 1
 #    ans = max(ans, window)
 # return ans
 pass

# Breakdown
# Start with empty window --> append 1 element from the right
# Everytime check if answer is still valid
# Update answer if valid --> does char meet conditions
# If invalid remove elements from the left until valid -->


# Example: Given an array (list) nums consited of only non-negative integers, find the largest sum among all subarrays of length k in nums

# If the input is nums = [1,2,3,7,4,1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by the [3,7,4] which sums to 14. 

def subarray_sum_fixed(nums: list[int], k:int) -> int:
  window_sum = 0 
  for i in range(k):
    window_sum += nums[i] # starting point to compare agiasnt
  largest = window_sum # current best (largest)
  for right in range(k, len(nums)):
    left = right - k # first (outside of window)
    window_sum -= nums[left] #dropped left
    window_sum += nums[right] #added  right
    largest = max(largest, window_sum)
  return largest # maximum sum of k length windows

# DYNAMIC SLIDING WINDOW: Textbook example
# Longest Substring without Repeating Characters

# Find the length of the longest substirng without repeating characters.

# Input: abccabcabcc
# Output: 3
# Explanation: The longest substrings are abc and cab, both of the length 3.

# Input: aaaabaaa
# Output: 2
# Explanation: ab is the longest substring, with a length 2. 

def longest_substring_without_repeating_characters(s: str) -> int:
   window = []
   longest = 0
   l = 0
   counter: dict[str, int] = defaultdict(int) # every char count = 0
   for r in range(len(s)):
     counter[s[r]] += 1
     while counter[s[r]] > 1:
       counter[s[l]] -= 1
       l += 1
     longest = max(longest, r - l + 1)
   return longest

   # init window
   # init current and next pointers
   # append current
   # compare with next if != then append
   # increment fast by one and do this again
   # if duplicate, slide left until not duplicates, once true
   # start sliding right again until duplicates or done. 


nums = [3, -2, 1, 4]




def minimum_sum_sub_array(nums: List[int], l: int, r: int) -> int:
  min_sum = 0

  for k in range(l, r + 1):
   # print(f'k: {k}')
   # print(f'nums[:k]: {sum(nums[:k])}')
    window_sum = sum(nums[:k])
    if window_sum > 0:
      min_sum = min(min_sum, window_sum)

    for r in range(k, len(nums)):
    #  print(f'k: {k}')
    # print(f'len(nums): {len(nums)}')
      print(f'r: {nums[r]} & r-1: {nums[r-1]}')
      window_sum += nums[r] - nums[r - k]
      print(window_sum)

      if window_sum > 0:
          min_sum = min(min_sum, window_sum)
    

  return min_sum if min_sum != 0 else -1

minimum_sum_sub_array(nums, 2, 3)