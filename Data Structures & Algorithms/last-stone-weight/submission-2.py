class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []  

        for stone in stones:
            heapq.heappush_max(max_heap, stone)
        
        while len(max_heap) > 1:
            stone1 = heapq.heappop_max(max_heap) #give us the heaviest rock
            stone2 = heapq.heappop_max(max_heap) # 2nd heaviest rock
            if stone1 != stone2:
                heapq.heappush_max(max_heap, stone1 - stone2)
        
        if max_heap:
            return max_heap[0]
        else:
            return 0        
        