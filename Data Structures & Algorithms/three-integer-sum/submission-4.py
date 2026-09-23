class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            j = i+1
            k = len(nums) - 1 
            while j<k:
                value = nums[i] + nums[j] + nums[k]
                if value == 0: #GOAL/DESIRED. 
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1 
                    while j<k and nums[j] == nums[j-1]: #duplicate!!!
                        j+=1 
                    while j<k and nums[k] == nums[k+1]: #duplicate!!!
                        k-=1 
                elif value < 0: 
                    j+=1 
                else:
                    k-=1
        return result
                    




