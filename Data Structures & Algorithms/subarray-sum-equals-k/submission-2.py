class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        result = 0
        hmap = {0:1}

        for num in nums:
            prefix += num 
            if prefix - k in hmap:
                result += hmap[prefix-k]
            hmap[prefix] = hmap.get(prefix, 0) + 1 
        
        return result

        