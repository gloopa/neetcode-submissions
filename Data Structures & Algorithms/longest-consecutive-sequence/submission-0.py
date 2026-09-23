class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = set(nums)
        length = 0
        for num in result:
            if num - 1 not in result:
                current = num
                count = 1
                while current + 1 in result:
                    current += 1
                    count +=1
                length = max(length, count)
        return length
        