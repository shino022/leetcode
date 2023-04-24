# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    cache = {} #{ # of nodes: [ a list of FBT ] }

    def dfs(n): #return all possible FBT with n nodes
      res = []
      if n == 1: #basecase
        return [TreeNode()]
      if n in cache:
        return cache[n]
      for l in range(1, n, 2):
        r = n - l - 1
        leftTrees, rightTrees = dfs(l), dfs(r)
        for leftTree in leftTrees: #Build all combinations
          for rightTree in rightTrees:
            res.append(TreeNode(0, leftTree, rightTree))
        cache[n] = res
      return res
    return dfs(n)