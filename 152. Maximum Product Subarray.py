class Solution:
  """
  The farther it goes from 0, the more likely it can turn the max in the end
  so keep track of max(pos) and min(neg) product

  pOPT(n) = maximum value ending at n
  nOPT(n) = min value ending at n
  pOPT(i) = max(nums[i] * pOPT(i - 1), nums[i], nums[i] * nOPT(i - 1))
  nOPT(i) = min(nums[i] * nOPT(i - 1), nums[i], nums[i] * pOPT(i - 1))
  """
  def maxProduct(self, nums: List[int]) -> int:
    curMin, curMax = 1, 1
    res = nums[0]
    for n in nums:
      temp = n * curMax
      curMax = max(n, temp, n * curMin)
      curMin = min(n, temp, n * curMin)
      res = max(res, curMax)
    return res
      