class Solution:
  """
  This algorithm checks if s1 is a permutation of any substring of s2.
  
  To do this, we initialize two counter arrays for s1 and the current substring of s2. Both arrays have length 26 to represent the 26 letters of the English alphabet. We then use a sliding window approach with left and right pointers to iterate through s2 and compare the counts of each letter in s1 and the current substring of s2.

  We first handle the edge case where the length of s1 is greater than the length of s2. If s1 is larger, then it cannot be a substring of s2.

  We then initialize the counts of s1 and the first substring of s2 of length s1. We compare the counts of each letter in both arrays to calculate the number of matching letters. If all 26 letters match, then s1 is a permutation of the substring and we return True.

  We then slide the window one letter to the right and update the counts and matching letters accordingly. We add the new letter at r to the substring at the right pointer and remove the leftmost letter at l. We compare the counts of the old and new letters in s1 and the substring to determine if the number of matching letters has increased or decreased.

  We continue to slide the window until the end of s2 is reached or s1 is found as a permutation of a substring. If s1 is found, we return True. Otherwise, we return False.
  """

  def checkInclusion(self, s1: str, s2: str) -> bool:
    # Handle edge case where len(s1) > len(s2)
    if len(s1) > len(s2):
      return False
      
    # Initialize counter arrays for s1 and s2
    count1, count2 = [0] * 26, [0] * 26

    # Initialize counts and matching letters for the first substring of s2
    for i in range(len(s1)):
      count1[ord(s1[i]) - ord('a')] += 1
      count2[ord(s2[i]) - ord('a')] += 1
    match = 0
    for i in range(26):
      if count1[i] == count2[i]:
        match += 1
    if match == 26:
      return True

    # Slide window through s2 and update counts and matching letters
    for r in range(len(s1), len(s2)):
      i = ord(s2[r]) - ord('a')
      count2[i] += 1
      if count1[i] == count2[i]:
        match += 1
      elif count1[i] + 1 == count2[i]:# decrement only when it becomes not equal
        match -= 1
      l = r - len(s1)
      i = ord(s2[l]) - ord('a')
      count2[i] -= 1
      if count1[i] == count2[i]:
        match += 1
      elif count1[i] - 1 == count2[i]: # decrement only when it becomes not equal
        match -= 1
      if match == 26:
        return True

    return False