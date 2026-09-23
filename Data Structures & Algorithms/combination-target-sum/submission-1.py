class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        temp=[]

        def dfs(start, targ):
            if targ == 0:
                result.append(temp[:])
            for i in range(start, len(nums)):
                 if nums[i] > targ:
                    break
                 temp.append(nums[i])
                 dfs(i, targ - nums[i])
                 temp.pop()
        dfs(0, target)
        return result
                


        