class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        minheap = []
        for key, value in hashmap.items():
            heapq.heappush(minheap, (value, key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        result = []
        for value, key in minheap:
            result.append(key)
        return result