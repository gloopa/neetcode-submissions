class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        
        valid = set() 

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if (val, 'row', r) in valid or (val, 'col', c) in valid or (val, 'box', (r//3, c//3)) in valid:
                        return False
                    valid.add((val, 'row', r))
                    valid.add((val, 'col', c))
                    valid.add((val, 'box', (r//3, c//3)))
        
        return True
        