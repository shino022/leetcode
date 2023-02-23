class Solution:
  """
  To implement this algorithm, we'll use two heaps: a minheap and a maxheap.
  The minheap will store pairs of (capital, profit), and we'll use it to keep
  track of all available projects. The maxheap will store the profits of the
  projects that we can currently afford to invest in.

  Here are the steps we'll follow:

  Initialize the minheap with all the available projects.
  Pop all the elements from the minheap that have capital less than or equal to
  our initial investment, w, and push their profits onto the maxheap.
  After this step, all the projects in the maxheap will have capital less than or equal to w.
  Pop the project with the maximum profit from the maxheap and add its profit to our investment, w.
  Repeat steps 2 and 3 k times, where k is the maximum number of projects we can invest in.

  Note: -sign is used to implement max heap because, heapq library only support min heap
  """
  def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    minHeap = [(capital, profit) for capital, profit in zip(capital, profits)]
    maxHeap = []
    heapq.heapify(minHeap)
    for n in range(k):
      while minHeap and minHeap[0][0] <= w:
        capital, profit = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, -profit)
      if maxHeap:
        w += -heapq.heappop(maxHeap)
    return w
