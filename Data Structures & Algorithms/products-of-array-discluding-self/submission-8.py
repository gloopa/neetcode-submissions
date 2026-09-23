class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod = 1 
        rightprod = 1 
        result = [-1] * len(nums)

        for i in range(len(nums)):
            result[i] = leftprod 
            leftprod *= nums[i] 
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= rightprod 
            rightprod *= nums[i]
        
        return result
        