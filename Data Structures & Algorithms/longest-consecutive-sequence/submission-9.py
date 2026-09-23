class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        count = 0
        length = 0

        for i in range(len(nums)):
            if nums[i]-1 not in numbers:
                count = 1
                while nums[i] + count in numbers:
                    count+=1
                length = max(length,count)
        
        return length 



        