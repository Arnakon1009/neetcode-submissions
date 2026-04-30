class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()
        for col in range(9):
            for row in range(9):
                if board[col][row] in check: return False
                if board[col][row] != ".": check.add(board[col][row])
            check.clear()
        
        for row in range(9):
            for col in range(9):
                if board[col][row] in check: return False
                if board[col][row] != ".": check.add(board[col][row])
            check.clear()

        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                for r in range(r_start, r_start + 3):
                    for c in range(c_start, c_start + 3):
                        val = board[r][c]
                        if val == ".": continue
                        if val in check: return False
                        check.add(val)
                check.clear()
        return True