# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
BFS using queue
while loop to iterate thru all nodes
  for loop to traverse a level
Edge case: if the root tree is empty, deosn't append to the queue
"""
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      res = []
      q = deque()
      if root:
        q.appendleft(root)
      while q:
        level = []
        for i in range(len(q)):
          node = q.pop()
          level.append(node.val)
          if node.left:
            q.appendleft(node.left)
          if node.right:
            q.appendleft(node.right)
        res.append(level)
      return res
