class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num in freqs:
                freqs[num]+=1 
            else:
                freqs[num] = 1 
       
        minheap = []

        for num, freq in freqs.items():
            heapq.heappush(minheap, (freq, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        result = []
        for freq, num in minheap:
            result.append(num)
        return result


        