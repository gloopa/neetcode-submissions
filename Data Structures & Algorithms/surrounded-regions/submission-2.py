class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r, c):
            if r<0 or c<0 or c>=col or r>=row:
                return 
            if board[r][c] != 'O':
                return 
            board[r][c] = 'T'
            for dr, dc in directions:
                nr = dr+r
                nc = dc+c
                dfs(nr,nc)
        

            

        for r in range(row):
            for c in range(col):
                if r == 0 or r == row-1 or c == 0 or c == col-1:
                    if board[r][c] == 'O':
                        #run dfs to find all the connected edge 'O's 
                        dfs(r,c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

        