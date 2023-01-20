""" 
init count{num: freq}
init freq[[num]] index is freq and value is an array of numbers
  the size of freq is up to len(nums)
swap value and index, and assign it to freq
  because a frequency has many number, it's stored as an array of numbers
  so freq will look like [[],[3],[2,1],[],[]] given nums = [1,1,2,2,3]
iterate over freq in reverse order(largest freq to small)
  concat the number to res (res += freq[i])
  stop if len(res) == k
return res
"""
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    res = []

    #count nums
    for n in nums:
      count[n] = 1 + count.get(n, 0)

    #swap number, and frequency and assign it to freq
    for n, f in count.items():
      freq[f].append(n)
    
    #iterating thru reverse order, concat until len(res) == k
    for i in range(len(freq)-1, -1, -1):
      res += freq[i]
      print(freq[i])
      if len(res) == k:
        break
    return res