class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap -> Key: number , Value: Frequency 
        freq = Counter(nums)
        minheap = []
        
        for key, val in freq.items():
            heapq.heappush(minheap, (val, key))
            if len(minheap) > k:
                heapq.heappop(minheap) 
        result = []
        for val, key in minheap:
            result.append(key)
        return result

            
        