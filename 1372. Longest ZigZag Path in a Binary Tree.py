
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  """
  Iterate using dfs
  store the previous direction
  we are going to go right and left both
  if the current direction is equal to the prev direction, then it starts from 1
  if the current direction is different from the prev dir, add 1 to total
  At each step, keep track of the total length of the current path and return the maximum of both paths 
  basecase: return total - 1 if it's null

  dfs(cur, prevRight, total):
    basecase:
      if null return total - 1
    if prevRight, theres 2 cases:
      return max(dfs(cur.left, False, total+1),dfs(cur.right, True, 1))
    if prevLeft, theres 2 cases:
      return max(dfs(cur.right, True, total+1),dfs(cur.left, True, 1))
      
  """
  def longestZigZag(self, root: Optional[TreeNode]) -> int:
    # Define dfs for iteration
    def dfs(cur, isPrevRight, total):
      if not cur:
        #substract one, bc we went one more step from the leaf node,
        return total - 1

      # Check left and right branches keeping track of the total lenth
      if isPrevRight:
        return max(dfs(cur.left, False, total + 1), dfs(cur.right, True, 1))
      else:
        return max(dfs(cur.right, True, total + 1), dfs(cur.left, False, 1))
    
    return max(dfs(root.right, True, 1), dfs(root.left, False, 1))
