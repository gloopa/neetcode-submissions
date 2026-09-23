class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Max heap -> head will be the highest value (priot by distance to 0,0)
        maxheap = []
        for x, y in points: 
            distance = math.sqrt((0 - x)**2 + (0 - y)**2)
            heapq.heappush_max(maxheap, (distance, (x,y)))
            while len(maxheap) > k:
                heapq.heappop_max(maxheap)
        result = []
        for dist, point in maxheap:
            result.append(point)
        return result


        
     


        