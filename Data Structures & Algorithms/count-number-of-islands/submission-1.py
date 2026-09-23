class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        row = len(grid)
        col = len(grid[0])
        islands = 0

        def dfs(r, c):
            if r<0 or r>= row or c<0 or c>=col: #out of bounds
                return 
            if grid[r][c] == '0': #water 
                return 
            grid[r][c] = '0'
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c 
                dfs(nr, nc)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    islands+=1 
                    dfs(r,c)
        
        return islands

        

        