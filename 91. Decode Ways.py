class Solution:
  """
  Bottom up solition with Time and Memory complexity of O(n)
  
  dp(n): num of ways from n 
  dp[i] = dp[i+1] + dp[i+2]

  if s[i] == 0, there's no way we can decode numbers starting from 0
  so dp[i] will be 0

  dp[i+2] will be only added when s[i] can be 2 digits
  """
  def numDecodings(self, s: str) -> int:
    dp = [0] * (len(s) + 1)
    dp[len(s)] = 1
    for i in range(len(s) - 1, -1, -1):
      if s[i] == "0":
        dp[i] = 0
      else:
        dp[i] = dp[i+1]
      
      # if there's an elem after i
      if i + 1 < len(s) and ( 
        s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
      ):
        dp[i] += dp[i+2]
    return dp[0]

    