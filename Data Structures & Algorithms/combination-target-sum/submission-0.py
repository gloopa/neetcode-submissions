class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        temp = []

        def dfs(start, targett):
            if targett == 0:
                result.append(temp[:])
            for i in range(start, len(nums)):
                if nums[i] > targett:
                    break
                temp.append(nums[i])
                dfs(i, targett - nums[i])
                temp.pop()
        dfs(0, target)
        return result