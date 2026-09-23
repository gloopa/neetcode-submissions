class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)] 
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        minute = 0
        
 
    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                  
        while queue:
            level_size = len(queue)
            rotten_round = False
            for _ in range(level_size):
                r, c = queue.popleft() 
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc 

                    if 0<= nr < row and 0<= nc < col and grid[nr][nc] == 1: #bounds 
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
                            rotten_round = True
            if rotten_round:
                minute+=1
        for r in range(row):
                for c in range(col):
                    if grid[r][c] == 1:
                        return -1
        return minute
            
        

            




        