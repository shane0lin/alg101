# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
from typing import List
import collections

def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = collections.defaultdict(set) # key: row, value: set of numbers
    cols = collections.defaultdict(set) # key: col, value: set of numbers
    squares = collections.defaultdict(set)  # key: (row // 3, col // 3), value: set of numbers
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True

