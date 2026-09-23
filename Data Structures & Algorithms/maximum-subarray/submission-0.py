class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = nums[0]

        for num in nums:
            currsum = max(num, currsum + num)
            maxsum = max(maxsum, currsum)
        return maxsum

            

        