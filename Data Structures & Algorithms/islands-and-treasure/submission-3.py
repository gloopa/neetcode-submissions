class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        row = len(grid)
        col = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    queue.append((r,c))
        
        while queue:
            r, c = queue.popleft() 
            visited.add((r,c))
            for dr, dc in directions:
                nr = dr+r
                nc = dc+c 
                if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 2147483647:
                    if (nr,nc) not in visited:
                        grid[nr][nc] = grid[r][c] + 1 
                        queue.append((nr,nc))
                    
            
        