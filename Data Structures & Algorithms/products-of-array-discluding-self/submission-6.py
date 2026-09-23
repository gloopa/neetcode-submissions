class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = 1
        rprod = 1
        result = [0] * len(nums)

        for i in range(len(nums)):
            result[i] = lprod 
            lprod = lprod * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= rprod
            rprod = rprod * nums[i]
        
        return result