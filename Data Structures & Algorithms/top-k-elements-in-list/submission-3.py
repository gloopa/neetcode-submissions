class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use hashmap to find frequency, then use min heap to find kth element via pop

        #part 1, frequency 
        hashmap = Counter(nums)
        
        #part 2, min heap 
        heap = []

        for num,freq in hashmap.items():
            heapq.heappush(heap, (freq, num)) #we added all the values in the minheap
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        
        for freq,num in heap:
            result.append(num)
        return result



        