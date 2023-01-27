class Solution:
  #dp(i): from i to end can be broken
  """
  s starting from 1
  dp[len] = True

  if it's inbound and have the same word and dp[i+len(w)] is True
  dp[i] is True and stop moving forward to the next word 

  ex) current i = 4, dp[4] = (inbound && dp[8] && s[4:8] == w)
    s         w     dp
    01234567  0123  012345678
    leetcode  code       FFFT
  """
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s)-1, -1, -1):
      for w in wordDict:
        if i + len(w) <= len(s) and w == s[i:i+len(w)] and dp[i+len(w)]:
          dp[i] = True
          break
    return dp[0]
        