# BINARY SEARCH: cut the problem in half at every step O(n) -> O(log n)

def binary_search(arr: list[int], target: int) -> int:
#  left, right = 0, len(arr) - 1
#  while left <= right:
#    mid = (left + right) // 2
#    if arr[mid] == target:
#       return mid # found target
#    elif arr[mid] < target:
#       left = mid + 1
#    else:
#       right = mid - 1
  return -1

# anytime looking for a number in a sorted array
# or a monotonic condition changes only in one direction

# for a non-sorted monotonic condition like FFFFFTTTTTT
def binary_search_non_numeric(arr: list[int], target: int) -> int:
 # left, right = 0, len(arr) - 1
 # first_true_index = -1
 # while left <= right:
 #   mid = (left + right) // 2
 #   if feasible(mid):
 #     first_true_index = mid
 #     right = mid - 1
 #   else:
 #     left = mid + 1

 # return first_true_index
  return -1



# FIND MINIMUM IN ROTATED SORTED ARRAY

def find_min_rotated(arr: list[int]) -> int:
  # left, right = 0, len(arr) - 1
  # boundary_index = -1

  # while left <= right:
  #  mid = (left + right) // 2
  #  if <= last element, then belongs to lower half
  #  if arr[mid] <= [arr[-1]]:
  #    boundary_index = mid
  #    right = mid - 1
  #  else:
  #    left = mid + 1
  # return boundary_index
  return 0