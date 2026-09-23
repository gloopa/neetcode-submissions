class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums) #all the unique values
        longest = 0 

        for num in sett:
            if num - 1 not in sett: #first value 
                count = 1
                iteration = 1
                while num + iteration in sett:
                    count+=1
                    iteration+=1
                longest = max(longest, count)
        return longest
        