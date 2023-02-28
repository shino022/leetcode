# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    # A dictionary to keep track of the frequency of each subtree
    subTrees = defaultdict(int)
    # A list to store the duplicate subtrees
    duplicates = []
    
    # A recursive function to traverse the tree
    def dfs(node):
      if not node:
        return None
      # A tuple representing the subtree rooted at this node
      t = (node.val, dfs(node.left), dfs(node.right))
      # If we've only seen this subtree once, add it to the duplicates list
      if subTrees[t] == 1:
        duplicates.append(node)
      # Increment the frequency of this subtree
      subTrees[t] += 1
      return t
  
    # Start the traversal from the root
    dfs(root)
    
    # Return the list of duplicate subtrees
    return duplicates