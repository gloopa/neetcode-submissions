class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = set()
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value != '.':
                    if (value, 'row',row) in valid or (value, 'col',col) in valid  or (value, 'box', (row//3, col//3)) in valid:
                        return False #since it already exists 
                    valid.add((value, 'row',row)) 
                    valid.add((value, 'col',col))
                    valid.add((value, 'box', (row//3, col//3)))
        return True


        