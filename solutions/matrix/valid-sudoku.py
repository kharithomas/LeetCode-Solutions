# TC: O(1), since board is fixed size
# SC: O(1)

from collections import defaultdict
from typing import List


class Solution:
    def getGroup(self, row: int, col: int) -> tuple:
        return (row // 3, col // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_with = defaultdict(set)
        cols_with = defaultdict(set)
        vals_in_group = defaultdict(set)

        # For each position determine if it's valid
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c])

                # If value at pos is duplicate
                if r in rows_with[val] or c in cols_with[val]:
                    return False

                # If value is duplicate in 3x3
                g = self.getGroup(r, c)
                if val in vals_in_group[g]:
                    return False

                vals_in_group[g].add(val)
                rows_with[val].add(r)
                cols_with[val].add(c)

        return True


s = Solution()
print(s.isValidSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
print(s.isValidSudoku(
    [["8", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
