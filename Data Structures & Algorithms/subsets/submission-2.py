class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def dfs(i):
            if i == len(nums):
                res.append(temp[:])
                return
            dfs(i+1)
            #pick
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
        dfs(0)
        return res


        