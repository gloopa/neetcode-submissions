class Solution:
    def findMin(self, nums: List[int]) -> int:
        #we want the pivot value, since that will be the lowest value
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if left == right:
                return nums[left]
            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid
           
     