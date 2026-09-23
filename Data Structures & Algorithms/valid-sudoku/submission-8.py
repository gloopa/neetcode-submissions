class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if (val, r, 'row') in valid or (val, c, 'col') in valid or (val, (r//3, c//3), 'box') in valid:
                        return False
                    valid.add((val, r, 'row'))
                    valid.add((val, c, 'col'))
                    valid.add((val, (r//3, c//3), 'box'))
        
        return True
        