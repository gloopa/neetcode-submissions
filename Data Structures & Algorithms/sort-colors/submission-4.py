class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1 
        third = 0
        while third <= right:
            if nums[third] == 0:
                nums[left], nums[third] = nums[third], nums[left]
                left+=1 
                third+=1
            elif nums[third] == 2:
                nums[right], nums[third] = nums[third], nums[right]
                right-=1
            else:
                 third+=1