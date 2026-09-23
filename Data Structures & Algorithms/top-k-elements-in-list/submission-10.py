class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = {}
        minheap = []

        for num in nums:
            if num in freqs:
                freqs[num] += 1 
            else:
                freqs[num] = 1 
        
        for num, fr in freqs.items():
            heapq.heappush(minheap, (fr, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        result = []
        for fr, num in minheap:
            result.append(num)
        return result