class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap = []

        for num in arr:
            distance = abs(x - num) 
            heapq.heappush_max(maxheap, (distance, num))
            while len(maxheap) > k:
                heapq.heappop_max(maxheap)
        result = []
        for distance, num in maxheap:
            result.append(num)
        return sorted(result)
        