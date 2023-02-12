"""
Here's a revised version of the algorithm description:
  This algorithm calculates the maximum profit that can be made from a given list of stock prices. 
  It uses dynamic programming and defines a hashmap that stores the index and the state (can buy or can sell) 
  as its key and the maximum profit as its value. 
  The max profit is calculated using a depth-first search (DFS) approach with the following 

DFS(index, state)
  base cases:
    1. If the index is out of bounds, 0 is returned, as no profit is made.
    2. If the result is already cached, the cached result is returned.

  There are two states in the algorithm:
    1. If the state is "can buy", there are two cases to consider:
      1. Buy the stock, in which case the profit is calculated as the result of the DFS applied to the next index with the state "can sell" minus the price at the current index.
      2. Wait, in which case the profit is calculated as the result of the DFS applied to the next index with the state "can buy". The case with the higher profit is selected and cached.
    2. If the state is "can sell", there are two cases to consider:
      1. Sell the stock, in which case the profit is calculated as the result of the DFS applied to the next index after the next with the state "can buy" plus the price at the current index.
      2. Wait, in which case the profit is calculated as the result of the DFS applied to the next index with the state "can sell". The case with the higher profit is selected and cached.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      dp = {}
      def dfs(i, canBuy):
        if i >= len(prices):
          return 0
        if (i, canBuy) in dp:
          return dp[(i, canBuy)]
        
        if canBuy:
          buyProfit = dfs(i+1, not canBuy) - prices[i]
          waitProfit = dfs(i+1, canBuy)
          dp[(i, canBuy)] = max(buyProfit, waitProfit)
        else:
          sellProfit = dfs(i+2, not canBuy) + prices[i]
          waitProfit = dfs(i+1, canBuy)
          dp[(i, canBuy)] =  max(sellProfit, waitProfit)
        
        return dp[(i, canBuy)]
      
      return dfs(0, True)
        