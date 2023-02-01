class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    """
     ace
    a0000
    b0111
    c0111
    d0122
    e0122
     0123 <--dp[m][n] is returned

    2 cases:
      dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1]) if text1[i] == text2[j]
      dp[i+1][j+1] = dp[i][j] + 1 if text1[i] != text2[j]
    """ 
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if text1[i - 1] == text2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1] + 1
          print(dp)
        else:
          dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
