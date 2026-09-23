class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result =[]
        temp = []

        def dfs(start, remain):
            if remain == 0: 
                result.append(temp[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                if candidates[i - 1] == candidates[i] and i > start:
                    continue
                temp.append(candidates[i])
                dfs(i+1, remain - candidates[i])
                temp.pop()
        dfs(0, target)
        return result