class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Have a dictionary/hashmap, where the key would be the number
        #and value would be it's corresponding index 
        #O(1) lookup, and O(N) search since for loop (n-1 ) times 
        hashmap = {} 
        for i, num in enumerate(nums):
            comp = target - num #the value we need -> search through dict 
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[num] = i
        


        