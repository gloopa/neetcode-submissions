class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        result = [1] * n

        for i in range(len(nums)):
            result[i] = prefix 
            prefix = prefix * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix 
            suffix *= nums[i]
        return result
        
            
          