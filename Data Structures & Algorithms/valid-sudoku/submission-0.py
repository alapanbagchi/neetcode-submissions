class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] in row_set[i] or board[j][i] in col_set[i] or board[i][j] in squares[(i//3, j//3)]:
                    return False
                if board[i][j] != '.':
                    row_set[i].add(board[i][j])
                if board[j][i] != '.':    
                    col_set[i].add(board[j][i])
                if board[i][j] != '.':
                    squares[(i//3, j//3)].add(board[i][j])
        return True
