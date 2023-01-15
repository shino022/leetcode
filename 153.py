"""
if it's not rotated, it's always nums[l] < nums[r] so you can return nums[l]
else if it's rotated, we have 2 cases
  we can see it as 2 portions
  1. if nums[m] > nums[r] or nums[l] < nums[m]
    in either case, pivot is in the right portion
  2. if nums[m] < nums[r] or nums[l] > nums[m]
    in either case, pivot is in the left portion
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
      l, r = 0, len(nums) - 1
      while l <= r:
        m = (l + r) // 2
        if nums[l] <= nums[r]:
          return nums[l]
        elif nums[m] > nums[r]:
          l = m + 1
        else:
          r = m 