# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2]
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

def find_min(nums):
  min_res = nums[0]

  for i,val in enumerate(nums, start=1):
    if val < min_res:
      min_res = val
  return min_res


def find_min_bst(nums):
  start = 0
  end = len(nums)

  min_res = None

  while start <= end:
    midpt = int((start + end) / 2)
    cur_val = nums[midpt]
    # print('start: {} end: {} midpt: {} cur_val: {}'.format(start, end, midpt, cur_val))
    if midpt in (0, len(nums) - 1): # [4,2] (0,2) [2,3,4,5,6]
      return cur_val
    prev_val = nums[midpt - 1]
    after_val = nums[midpt + 1]
    if after_val < cur_val:
      return after_val

    if prev_val > cur_val:
      return cur_val

    if nums[0] < cur_val:
      # Check left
      end = midpt
    else:
      # Check right
      start = midpt + 1



# arr = [5,6,7,3,4]
arr = [1,2,3,4,5]

min_res = find_min_bst(arr)
print(min_res)
