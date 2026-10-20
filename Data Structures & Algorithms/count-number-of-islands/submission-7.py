class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        rows,cols = len(grid), len(grid[0])
        count = 0
        def bfs(r,c):
            queue = deque([(r,c)])
            while queue:
                r,c = queue.popleft()

                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c 

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] != '0' and (nr,nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count+=1
                    bfs(r,c)

        return count