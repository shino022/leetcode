"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
Use hashmap that map old to new, it also keeps track of visited node
Deep Copy using dfs

Edge case:
  when an empty graph is given, it will run dfs(null)

dfs(node):
  Basecase:
    if visited, that means it has a copy so return the copy

  Not visited:
    create a copy
    iterating thru all neighbors, append the copy version of it's neighbors

    return the copied node
"""
class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    oldToNew = {}

    def dfs(n):
      if n in oldToNew:
        return oldToNew[n]

      newNode = Node(n.val)
      oldToNew[n] = newNode
      for neighbor in n.neighbors:
        newNode.neighbors.append(dfs(neighbor))
      return newNode
      
    return dfs(node) if node else None
