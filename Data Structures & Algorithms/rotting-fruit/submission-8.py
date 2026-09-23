class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque() 
        fresh = 0 

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1 
                elif grid[r][c] == 2:
                    queue.append((r,c))
        directions = [(1,0), (0,1), (-1,0),(0, -1)]
        minute = 0

        while queue and fresh > 0:
            for _ in range(len(queue)): #minute 
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1 
                        queue.append((nr,nc))
            minute += 1 
        
        if fresh:
            return -1
        else:
            return minute
            
                



        