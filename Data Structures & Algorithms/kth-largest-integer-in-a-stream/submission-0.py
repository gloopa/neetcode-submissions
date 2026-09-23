class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums 
        heapq.heapify(self.nums)
        self.minheap = self.nums
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
    


        
