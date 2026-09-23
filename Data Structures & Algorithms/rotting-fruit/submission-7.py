class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        visited = set()
        mins = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    queue.append((r,c))

        while queue:
            level_length = len(queue)
            isRotten = False
            for _ in range(level_length):
                r, c = queue.popleft()
                visited.add((r,c)) 
                for dr, dc in directions:
                    nr = dr+r
                    nc = dc+c
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        grid[nr][nc] = 2 
                        queue.append((nr,nc))
                        isRotten = True 
            if isRotten:
                mins+=1 
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
        return mins


        