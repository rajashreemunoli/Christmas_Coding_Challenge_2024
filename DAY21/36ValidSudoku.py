#36. Valid Sudoku
#  Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:
#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

def isValidSudoku(board):
        N = 9
        rowSet = [set() for _ in range(N)]
        colSet = [set() for _ in range(N)]
        squareSet = [set() for _ in range(N)]
        

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".": continue
                sr, sc = r // 3, c // 3
                sPos = sr * 3 + sc
                if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in squareSet[sPos]:
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[sPos].add(board[r][c])

        return True

board1=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

if isValidSudoku(board1):
     print("Board 1 is a valid Sudoku board.")
else:
     print("Board 1 is not a valid Sudoku board.")

board2=[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
if isValidSudoku(board2):
     print("Board 2 is a valid Sudoku board.")
else:
     print("Board 2 is not a valid Sudoku board.")