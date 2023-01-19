"""
Decision tree
[1, 2, 3]      
3 layers

In ith layer it appends ith elem to the current subset or doesn't append anything
when it reaches to the leaf node (i >= len(nums)),
it appends the subset to the result as a copy (bc it's a reference)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      res = []
      def dfs(i, cur):
        if i >= len(nums):
          res.append(cur.copy())
          return
        cur.append(nums[i])
        dfs(i + 1, cur)
        cur.pop()
        dfs(i + 1, cur)
      dfs(0, [])
      return res