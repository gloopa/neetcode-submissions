class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        count = 0
        res = 0
        for num in nums:
            if num-1 not in arr:
                #start
                count = 1
                while num+count in arr:
                    count+=1 
                res = max(res, count)
        
        return res
                


        