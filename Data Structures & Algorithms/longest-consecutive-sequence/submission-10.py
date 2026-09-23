class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elem = set(nums)
        count = 0
        length = 0
        for num in elem:
            if num-1 not in elem:
                count = 1 
                while num+count in elem:
                    count+=1 
                length = max(length, count)
        
        return length
        