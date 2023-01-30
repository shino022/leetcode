class Solution:
  def change(self, amount: int, coins: List[int]) -> int:
    """
    dp[i][w]
    dp[i][amount]: # of comb using coins up to i
    dp[i][amount] = dp[c-1][w] (+ dp[c][w-c] if w - c >= 0)
    Input: amount = 5, coins = [1,2,5]
    Init dp[i][amount]
      0 1 2 3 4 5
    0 1 0 0 0 0 0
    1 1 
    2 1 
    5 1 
    Imp
      0 1 2 3 4 5
    0 1 0 0 0 0 0
    1 1 1 1 1 1 1
    2 1 1 2 2 3 3
    5 1 1 2 2 3 4
    """
    dp = [[0] * (amount + 1) for i in range(len(coins)+1)]
    for i in range(len(coins) + 1):
      dp[i][0] = 1

    for i in range(1, len(coins)+1):
      c = coins[i-1]
      for w in range(1, amount+1):
        dp[i][w] = dp[i - 1][w]
        if w - c >= 0:
          dp[i][w] += dp[i][w - c]

    return dp[len(coins)][amount]
