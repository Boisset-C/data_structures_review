
# HASH MAPS: LOOKUP & INSERT: Average O(1) 

hashmap = dict() # uses hash function to create a value that represents memory address

# collisions can happen theoritically but usually they are handled
# keys must be hashable
# - Numbers
# - Strings
# - Tuples

# Not hashable
# - Lists
# - Dictionaries

# USECASE: Finding a value that already exists
# - No Hash Map = O(n)
# - Hash Map = O(1)

# when solving problems throug brute force ask the same question again and again
# when solving using hashmap remember the answer as you go 
data = "bunch of data"

# Implementing a Hash Map in CODE: (FREQUENCY MAP)

my_map = {} # Step 1: Storing something:

for item in data: # Step 2: Looking something up: 
   if item not in my_map: # Step 3: Updating/initializing values:
      my_map[item] = 1
   else:
      my_map[item] += 1

# in python helper for this is defaultdict in python
# hash maps are often used while you loop, helping a O(n^2) solution turn into O(n) becasue then you loop once
# initialize a map, use it while looping and get fast lookup & storage.



# Example: TWO SUM PROBLEM
# Brute force solution is nested for loops O(n^2)
# OPTIMAL IS TO USE A HASH MAP O(n)
# input: nums array & target
nums = [1,2,3,4,5,6]
target = 11

# output: indices of two summands that give target
def optimal_two_sum_finder(array, target):
   nums_to_index = {}

   for i, num in enumerate(array): # we want index + element so we use enumerate
      complement = target - num # find potential target

      if complement in nums_to_index: # check if we have
         print(f'Here are two indices of the summands that add to the target: {[nums_to_index[complement], i]}')
         return [nums_to_index[complement], i]

      nums_to_index[num] = i

   return []

optimal_two_sum_finder(nums, target)


# time complexity O(n) might need to go through each elements at least once
# space complexity O(n) might need to store each elements atleast once















