class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        length = 0
        for i, num in enumerate(nums):
            if num != num-1:
                count = 1 #start 
                while num + count in set(nums):
                    count+=1
                length = max(length, count)
        return length 




        