class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        count = 0
        result = 0
        for num in seen:
            if num-1 not in seen:
                count = 1 #starting 

                while num+count in seen: 
                    count+=1 
                result = max(result, count)
            
        return result


        