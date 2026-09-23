class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 

        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                if hashmap[comp] >= i:
                    return [i, hashmap[comp]]
                else:
                    return [hashmap[comp], i]
            hashmap[num] = i
        
        