"""
This code uses a binary search approach to find the pivot element in a rotated array.
If the array is not rotated, nums[l] will always be less than nums[r], so we can return nums[l] as the pivot.
If the array is rotated, we have two cases:
  1. If nums[m] > nums[r] or nums[l] < nums[m], the pivot is in the right portion of the array.
  2. If nums[m] < nums[r] or nums[l] > nums[m], the pivot is in the left portion of the array.
This algorithm will find the pivot element of a rotated array in O(log n) time complexity and O(1) of memory.
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