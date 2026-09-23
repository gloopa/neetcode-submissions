class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use hashmap to find frequency, then use min heap to find kth element via pop

        #part 1, frequency 
        hashmap = Counter(nums)
        
        #part 2, min heap 
        heap = []

        for key,value in hashmap.items():
            heapq.heappush(heap, (value, key)) #we added all the values in the minheap
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        
        for key, value in heap:
            result.append(value)
        return result



        