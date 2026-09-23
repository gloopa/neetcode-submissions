class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1 
            else:
                freq[num] = 1 
        minheap = []
        result = []
        for num, f in freq.items():
            heapq.heappush(minheap, (f, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        for f, num in minheap:
            result.append(num)
        return result
        


        
