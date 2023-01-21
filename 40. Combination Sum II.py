class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      """
      Backtracking O(2^n) at least
      so sorting which takes O(nlogn) deosn't affect to the time complexcity.
      make a decision puckup or drop the current elem
      the subtree that dropped the current element will
      never used the ones repeated cuz it will generate duplicate
      ex)given [1, 1, 1]
        except for the left most branch [1], [11], [111] 
        everything else is duplecate
          [1]             []
      [11]   [1]      [1]     []
   [111][11] [11][1] [11][1]  [1][]
      """
      res = []
      candidates.sort()
      def dfs(i, cur, total):
        if total == target:
          res.append(cur.copy())
          return
        elif total > target or i >= len(candidates):
          return
        #select the elem
        cur.append(candidates[i])
        #move pointer forward
        dfs(i + 1, cur, total + candidates[i])
        #drop the elem
        cur.pop()
        #move pointer forward until the next value is not the same
        while (i < len(candidates) - 1 and 
          candidates[i] == candidates[i+1]):#??
          i += 1
        #move pointer to the next(diff value from the current elem)
        dfs(i + 1, cur, total)
      dfs(0, [], 0)
      return res


