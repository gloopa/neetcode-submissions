class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        size = float('inf')
        left = 0
        currsum = 0
        for right in range(len(nums)):
            currsum += nums[right]
            
            while currsum >= target:
                currsum -= nums[left]
                size = min(size, right - left + 1)
                left+=1 
            

        if size == float('inf'):
            return 0
        else:
            return size