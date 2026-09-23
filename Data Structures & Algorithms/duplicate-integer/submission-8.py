class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set -> gets rid of duplicates
        # if length of set is not equal to length of original nums, then there is a duplicate 

        seen = set()
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        
        return False