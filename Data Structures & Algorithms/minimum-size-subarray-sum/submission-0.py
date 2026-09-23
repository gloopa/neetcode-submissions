class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')

        left = 0
        summ = 0
        for right in range(len(nums)):
            summ += nums[right]
            while summ >= target:
                length = min(length, right - left + 1)
                summ -= nums[left]
                left+=1 
        
        return 0 if length == float('inf') else length
                
