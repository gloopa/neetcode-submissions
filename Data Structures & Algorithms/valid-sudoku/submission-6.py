class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #(2, 'row', row) (2,'row', col), (2, 'box',)
        seen = set() #  (#, 'row or column or box', what row or column) -> row and col could have same values
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != '.':
                    if (val, 'row', row) in seen or (val, 'col', col) in seen or (val, 'box', (row//3, col//3)) in seen:
                        return False
                    seen.add((val, 'row', row))
                    seen.add((val, 'col', col))
                    seen.add((val, 'box', (row//3, col//3)))

        return True 

