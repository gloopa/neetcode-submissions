class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        minheap = []

        for num, fr in freq.items():
            heapq.heappush(minheap, (fr, num))
            while len(minheap) > k:
                heapq.heappop(minheap)
        result = []
        for fr, num in minheap:
            result.append(num)
        return result
        