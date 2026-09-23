class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #check duplicates via if previous number == current, and is in the same level
        #to only use a specific number ONCE, we can add 1 to recursive call to change to next number
        candidates.sort()
        result = []
        temp = []

        def dfs(start, remain):
            if remain == 0: #base case, it sums up to target value since we find complement
                result.append(temp[:])
            for i in range(start, len(candidates)):
                if candidates[i] == candidates[i-1] and i > start: #duplicates
                    continue
                if candidates[i] > remain:
                    break
                temp.append(candidates[i])
                dfs(i+1, remain - candidates[i])
                temp.pop()
        dfs(0, target)
        return result


        