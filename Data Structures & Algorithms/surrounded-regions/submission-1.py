class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        

        def dfs(r,c):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            if r<0 or c<0 or r>=row or c>=col:
                return 
            if board[r][c] == 'T' or board[r][c] == 'X':
                return 
            board[r][c] = 'T'
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc 
                dfs(nr, nc)

            

        for r in range(row):
            for c in range(col):
                if r==0 or c==0 or r == row-1 or c == col-1:
                    if board[r][c] == 'O':
                        dfs(r,c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
    
       
                    
        