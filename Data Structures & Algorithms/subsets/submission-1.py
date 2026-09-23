class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
         result = []
         temp = []
         n = len(nums)
         
         def back(i):
            if i == n:
                result.append(temp[:])
                return
            back(i+1)

            temp.append(nums[i])
            back(i+1)
            temp.pop()
         back(0)
         return result
        
        