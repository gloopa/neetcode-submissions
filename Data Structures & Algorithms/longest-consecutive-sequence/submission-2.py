class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        length = 0
        value = 0
        for num in sett:
            if num - 1 not in sett:
                length = 1
                iteration = 1
                while num + length in sett:
                    length += 1
                    iteration += 1
                value = max(value, length)
        
        return value




        