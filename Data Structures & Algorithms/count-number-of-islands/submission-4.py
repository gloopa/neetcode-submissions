class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        count = 0

        def dfs(r, c):
            if r<0 or c<0 or r>=row or c>=col:
                return 0
            if grid[r][c] == "0":
                return 0
            grid[r][c] = "0"
            for dr, dc in directions:
                nr = dr + r 
                nc = dc + c
                dfs(nr,nc)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    count+=1 
                    dfs(r, c)
        return count
                    
        

        