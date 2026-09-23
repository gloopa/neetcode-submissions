class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol = []
        n = len(nums)
        
        def back(i):
            if i == n: #we hit leaf node
                res.append(sol[:])
                return
            #do not pick i
            back(i+1)
            #do pick i
            sol.append(nums[i])
            back(i+1)
            sol.pop()
        back(0)
        return res