class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid #this returns index of mid 
            elif nums[mid] > nums[right]: #pivot is to the right, rotated arra
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
    
                else:
                    right = mid - 1
        return -1


#nums = [3,4,5,6,1,2,], target = 1

        