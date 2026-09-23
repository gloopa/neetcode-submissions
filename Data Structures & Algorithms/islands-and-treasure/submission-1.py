class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0: # treasure chest 
                    queue.append((r,c))

        
        while queue:
            r, c = queue.popleft() 
            for dr, dc in direction:
                nr = r + dr 
                nc = c + dc 
                if 0<=nr < row and 0<=nc <col:
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr, nc))
        
       
        



        


        




        
        