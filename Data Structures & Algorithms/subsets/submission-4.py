class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def back(i):
            if i == len(nums):
                res.append(temp[:])
                return
            back(i+1)
            temp.append(nums[i])
            back(i+1)
            temp.pop()
        back(0)
        return res
        