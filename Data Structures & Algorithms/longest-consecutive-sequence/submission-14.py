class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valid = set(nums)
        length = 0

        for num in valid:
            if num-1 not in valid:
                count = 1 
                while num+count in valid:
                    count+=1 
                length = max(length, count)

        return length

        