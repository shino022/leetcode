"""
Use dfs
mark if it can flow to the Pac or Atl
return cells that satisfy both conditions

starting from cells adj to ocean,
run dfs for neighbors that can flow water to the current cell
P P P P
P
P
P
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      def dfs(ocean, i, j):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ocean[i][j] = True
        for r, c in directions:
          if ( 0 <= i + r < m and 
            0 <= j + c < n and
            not ocean[i + r][j + c] and
            heights[i][j] <= heights[i + r][j + c] ):      
            dfs(ocean, i + r, j + c)

      m, n = len(heights), len(heights[0])

      pacific = [[True if i == 0 or j == 0 else False for j in range(n)] for i in range(m)]
      atlantic = [[True if i == m - 1 or j == n - 1 else False for j in range(n)] for i in range(m)]
      res = []

      #Find Pacific
      #Left side
      for i in range(m):
        dfs(pacific, i, 0)
      #Top side
      for j in range(n):
        dfs(pacific, 0, j)

      #Find Atlantic
      #Right side
      for i in range(m):
        dfs(atlantic, i, n - 1)
      #Bottom side
      for j in range(n):
        dfs(atlantic, m - 1, j)

      #Find coordinates that satisfy both
      for i in range(m):
        for j in range(n):
          if pacific[i][j] and atlantic[i][j]:
            res.append([i, j])
      
      for i in range(m):
        print(pacific[i])

      return res
