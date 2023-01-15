  """
  This uses the binary search algorithm
  Given a rotated array, it splits the array in half and
  checks if nums[m] == target and which part is in order.
  if left part is in order, you have 2 cases
    1.if nums[l] <= target < nums[m], target is in the left part
    2.else, target is in the right part
  if right part is in order, you have 2 cases
    1.if nums[m] < target <= nums[r], target is in the right part
    2.else, target is in the left part
  if the garget is not found, return -1

  This algorithm will find the index of the target in O(log n) time complexity with O(1) of memory.
  """
class Solution:
    def search(self, nums: List[int], target: int) -> int:
      l, r = 0, len(nums) - 1
      while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
          return m
        #left sorted
        if nums[l] <= nums[m]:
          if nums[l] <= target < nums[m]:
            r = m - 1
          else:
            l = m + 1
        else:
          if nums[m] < target <= nums[r]:
            l = m + 1
          else:
            r = m - 1
      return -1
