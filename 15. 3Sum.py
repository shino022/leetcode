class Solution:
  """
    To avoid generating duplicates later, we sort the input array at the beginning. 
    Then, we use three pointers and a nested loop to solve the problem.

    We start a for loop, where the first pointer 'c' goes up to the third last element. 
    However, we skip 'c' if it's the same as the previous element to prevent duplicates.

    Now, the problem is reduced to finding 2sum with a sorted array. 
    We use two pointers 'l' and 'r' to point to the second and last elements respectively. 

    We will loop thru the array using while loop until l and r meet
    In the while loop, we have three cases:
      If 'l' + 'r' + 'c' is too large, we shift 'r' to the left.
      If 'l' + 'r' + 'c' is too small, we shift 'l' to the right.
      If 'l' + 'r' + 'c' == 0, we append it to the result array and update 'l' until it's not the same as prev value.
    
    return the result array
  """
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    for i, c in enumerate(nums):
      #'i > 0' is added to handle edge case 'nums[0 - 1]'
      if i > 0 and c == nums[i - 1]:
        continue
      
      l, r = i + 1, len(nums) - 1
      while(l < r):
        threeSum = nums[l] + nums[r] + c
        if threeSum > 0:
          r -= 1
        elif threeSum < 0:
          l += 1
        else: # If result found
          res.append([nums[l], nums[r], c])
          l += 1
          while nums[l] == nums[l - 1] and l < r:
            l += 1
        
    return res
