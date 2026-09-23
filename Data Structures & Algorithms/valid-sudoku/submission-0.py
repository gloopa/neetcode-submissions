class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = set()
        
        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value != '.':
                    if(value , 'row',row ) in valid or (value , 'column', column) in valid or (value , 'box', (row//3, column//3)) in valid:
                        return False
                    valid.add((value , 'row',row ))
                    valid.add((value , 'column', column))
                    valid.add((value , 'box', (row//3, column//3)))
        
        return True



        