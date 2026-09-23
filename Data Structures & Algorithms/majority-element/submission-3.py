class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_count = 0

        for key, value in count.items():
            if value > max_count:
                max_count = value
                element = key
        
        return element

        

        
        