class Solution:
  """
  dfs with a adjacency list (index: course, value: a list of prerequisites)
  start from the all the possible nodes, cua we dont know where to start, and there can be multiple groups 
  dfs:
    Basecase: 1. nomore prereqs -> true, 2. already visited(to detect cycle) -> false
    Update visited to True
    Traverse all neighbor: once a Flase detected -> return Flase
    At this point, all prereq can be finished -> 
      1. update visited to False
      2. adj to empty (DP: nextime it's visited just return True)
      3. return True  
  """
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = [ [] for i in range(numCourses) ]
    print(adj, numCourses, prerequisites)
    visited = set() # only used for the cycle detection
    for c, p in prerequisites:
      adj[c].append(p)
    
    def dfs(i):
      # basecase: 1. nomore prereqs -> true, 2. already visited(to detect cycle) -> false
      if adj[i] == []:
        return True
      if i in visited:
        return False
      # update visited to True
      visited.add(i)
      # traverse all neighbor: once a Flase detected -> return Flase
      for pre in adj[i]:
        if not dfs(pre):
          return False
      
      # at this point, all prereq can be finished -> 
      #   1. update visited to False
      #   2. adj to empty (DP: nextime it's visited just return True)
      #   3. return True
      visited.remove(i)
      adj[i] = []
      return True
    for pre in range(numCourses):
      if not dfs(pre):
        return False
    return True
      