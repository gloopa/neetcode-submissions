class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2) 
            heapq.heappush_max(maxheap, (distance, point))
            if len(maxheap) > k:
                heapq.heappop_max(maxheap)
        res = []
        for distance, point in maxheap:
            res.append(point)
        return res


        