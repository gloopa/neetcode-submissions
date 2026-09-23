class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # result = [0, 0, 0, 0] 
        #          [1, 1, 2, 8]
        #          [48, 24, 12, 8]

        leftprod = 1 
        rightprod = 1 
        result = [0] * len(nums)

        for i in range(len(nums)):
            result[i] = leftprod 
            leftprod = leftprod * nums[i] #for the next value (since we aren't including current value to product) 
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= rightprod
            rightprod = rightprod * nums[i]
        
        return result
