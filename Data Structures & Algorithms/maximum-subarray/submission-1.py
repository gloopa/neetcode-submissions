class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        currsum = 0

        for num in nums:
            currsum = max(num, currsum + num)
            result = max(result, currsum)
        return result


        