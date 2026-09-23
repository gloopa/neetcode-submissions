class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        result = []
        for num, freq in freqs.items():
            if freq > len(nums) // 3:
                result.append(num)
        
        return result

        