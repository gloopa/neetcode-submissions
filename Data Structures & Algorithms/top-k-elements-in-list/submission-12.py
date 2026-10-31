class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        minheap = []

        for num, fr in freqs.items():
            heapq.heappush(minheap, (fr, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        ans = []
        for fr, num in minheap:
            ans.append(num)
        
        return ans
