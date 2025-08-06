# TC: O(n^2), where n is # of rows/cols
# SC: O(1)

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = cols = len(mat)
        res = 0

        # sum primary diagonal
        for i in range(rows):
            res += mat[i][i]

        # sum secondary diagonal
        for r in range(rows):
            for c in range(cols):
                if r == cols - 1 - c:
                    res += mat[r][c]

        # remove center
        if rows % 2 == 1:
            m = rows // 2
            res -= mat[m][m]

        return res


s = Solution()
print(s.diagonalSum(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]))
print(s.diagonalSum(
    [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]]))
print(s.diagonalSum([[5]]))
