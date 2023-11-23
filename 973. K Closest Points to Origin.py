class Solution:
  """
  Init maxheap: [(-distance, [x, y])] 
    store pairs, distance as a key but distance is stored in negative number bc of the nuture of heapq module (min heap my default)
  loop it:
    1. less than k elems in maxHeap -> push
    2. (k elems in maxHeap &&
       the current distance is smaller than the max distance in the heap) -> replace
  """
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    def getDistance(point):
      return math.sqrt(point[0]**2 + point[1]**2)
    
    maxHeap = [(-getDistance(points[0]), points[0])]
    
    for i in range(1, len(points)):
      point = points[i]
      distance = getDistance(point)
      maxDistance = -maxHeap[0][0]

      if len(maxHeap) == k and distance < maxDistance: 
        heapq.heapreplace(maxHeap, (-distance, point))
      elif len(maxHeap) < k:
        heapq.heappush(maxHeap, (-distance, point))
      
    return [point for distance, point in maxHeap]
      