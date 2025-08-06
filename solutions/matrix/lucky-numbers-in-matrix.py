# TC: O(m*n)
# SC: O(m*n)

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        mins, maxes = set(), set()
        res = []

        # row mins
        for r in range(rows):
            mins.add(min(matrix[r]))

        # col maxes
        for c in range(cols):
            max_col = matrix[0][c]
            for r in range(rows):
                max_col = max(max_col, matrix[r][c])
            maxes.add(max_col)

        # find all intersections
        for m in mins:
            if m in maxes:
                res.append(m)

        return res


s = Solution()
print(s.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(s.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(s.luckyNumbers([[7, 8], [1, 2]]))
