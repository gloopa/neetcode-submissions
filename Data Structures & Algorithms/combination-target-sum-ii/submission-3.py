class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sol = []
        def back(start, remain):
            if remain == 0:
                res.append(sol[:])
                return 
            for i in range(start, len(candidates)):
                if candidates[i] > remain: #if current num is greater than target val, pass
                    break 
                if candidates[i-1] == candidates[i] and i > start:
                    continue
                sol.append(candidates[i])
                back(i+1, remain - candidates[i])
                sol.pop()
        back(0, target)
        return res
        
        