class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []

        def back(i):
            if i == len(nums):
                result.append(temp[:])
                return
            
            back(i+1)
            temp.append(nums[i])
            back(i+1)
            temp.pop()
        back(0)
        return result
        