"""
i: the index of the current person

From 0 to k people are gonna take min of tickets[i] or tickets[k] seconds 
until tickets[k] finishes buying all tickets

From k+1 to the last people are gonna take either min of tickets[i] or tickets[k]-1 seconds becuase when the ticket[k] turn 0, following elements have 1 more tickets in the end.

Sum count

Ex) given k = 3
Index       0  1  2  3  4  5
Tickets    [1, 9, 2, 6, 3, 8]
Time taken [1, 6, 2, 6, 3, 5]
The elements at index 5 takes 5 seconds (tickets[k] - 1) becuase the execution ends in the middle of tickets[k]th iteration and elems before k don't count in the last iteration

tickets[0~k] takes min(tickets[k], ticket[i])
tickets[k+1~end] takes min(tickets[k]-1, ticket[i])

Time complexity O(n)
"""
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
      res = 0
      for i in range(len(tickets)):
        if i <= k:
          res += min(tickets[i], tickets[k])
        else:
          res += min(tickets[i], tickets[k] - 1)
      return res