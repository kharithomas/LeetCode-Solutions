# TC : O(m*n)
# SC : O(m+n)

from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for r in range(n):
            row_set, col_set = set(), set()

            for c in range(n):
                row_set.add(matrix[r][c])
                col_set.add(matrix[c][r])

            if len(row_set) != n or len(col_set) != n:
                return False

        return True


s = Solution()
print(s.checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
print(s.checkValid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]))
