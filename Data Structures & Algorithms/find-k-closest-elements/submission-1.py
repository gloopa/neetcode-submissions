class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        maxheap = [] 


        for i, num in enumerate(arr):
            heapq.heappush_max(maxheap, (abs(num-x), num)) 

            while len(maxheap) > k:
                heapq.heappop_max(maxheap)
        
        result = []
        
        for i, j in maxheap:
            result.append(j)
        
        return sorted(result)

        