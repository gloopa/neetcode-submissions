class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() #adjacentency
        result=[]
        temp = []

        def dfs(start, remain):
            if remain == 0: #base case
                result.append(temp[:])
            for i in range(start, len(nums)):
                if nums[i] > remain: #too large
                    break #since the next index ... will also be greater since we sorted it 
                
                temp.append(nums[i])
                dfs(i, remain - nums[i])
                temp.pop()
        dfs(0, target)
        return result
        