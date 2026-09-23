class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0 
        row, col = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r<0 or r>=row or c<0 or c>=col:
                return 0
            if grid[r][c] == 0:
                return 0 
            grid[r][c] = 0
            area = dfs(r+1, c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r, c-1) + 1 
            return area
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, dfs(r,c))
        
        if maxarea:
            return maxarea
        else:
            return 0

        