"""
Topological sort algo
Initialize a map crs to pre
dfs(crs)
  Basecases
    if visited, return False to prevent looping
    if there's no prerequisites, return True

  mark it visited

  for pre in prerequisites 
    if any loop found by recursive calling dfs(pre), return false
    
  if no loop detected 
    mark it unvisited
    remove all prerequisites so that it can return true, next time visited
    return true

run dfs for all crs bc some node can be disconnected
  if any dfs(crs) false return false
if no false, return true
"""
class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    crsToPre = { i: [] for i in range(numCourses) }
    visited = set()
    for crs, pre in prerequisites:
      crsToPre[crs].append(pre)

    def dfs(crs):
      if crs in visited: 
        return False
      if crsToPre[crs] == []: 
        return True

      visited.add(crs)

      for pre in crsToPre[crs]:
        if not dfs(pre):
          return False
      
      visited.remove(crs)
      crsToPre[crs] = []

      return True

    for crs in range(numCourses):
      if not dfs(crs):
        return False
    return True
