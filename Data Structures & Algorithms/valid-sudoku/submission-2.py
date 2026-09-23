class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #duplicates === USE SETTTTTTTTT
        valid = set()
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value != '.':
                    if (value, 'row', r) in valid or (value, 'col', c) in valid or (value, 'box', (r//3, c//3)) in valid:
                        return False
                    valid.add((value, 'row', r))
                    valid.add((value, 'col', c))
                    valid.add((value, 'box', (r//3, c//3)))
        return True
        