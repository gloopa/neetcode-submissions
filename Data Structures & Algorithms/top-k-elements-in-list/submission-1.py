class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap -> heap
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        minheap = []
        for key, value in freq.items():
            heapq.heappush(minheap, (value, key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        result = []
        for key, value in minheap:
            result.append(value)
        return result


          
