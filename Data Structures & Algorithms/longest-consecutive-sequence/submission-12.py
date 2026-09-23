class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums) #no duplicates 
        result = 0
        count = 0
        for num in new:
            if num-1 not in new:
                count = 1 
                while num+count in new:
                    count+=1
                result = max(result, count)
        return result



        