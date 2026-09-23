class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [] 
        for stone in stones:
            heapq.heappush_max(maxheap, stone)

        while len(maxheap)>1: 
            stone1 = heapq.heappop_max(maxheap)
            stone2 = heapq.heappop_max(maxheap)

            if stone1 != stone2:
                heapq.heappush_max(maxheap, stone1-stone2) 
        
        if maxheap:
            return maxheap[0]
        else:
            return 0

        