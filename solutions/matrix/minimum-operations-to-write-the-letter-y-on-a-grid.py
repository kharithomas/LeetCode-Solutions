# TC: O(m*n)
# SC: O(1)

from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        y, rest = [0]*3, [0]*3

        for r in range(n):
            for c in range(n):
                if (r == c or r + c == n - 1) and r < n // 2:
                    # cells in upper left/right diagonal of "Y"
                    y[grid[r][c]] += 1
                elif r >= n // 2 and c == n // 2:
                    # cells in bottom "Y"
                    y[grid[r][c]] += 1
                else:
                    # cells not in "Y"
                    rest[grid[r][c]] += 1

        res = float('inf')
        y_nums = sum(y)
        r_nums = sum(rest)

        # try all 9 combinations to find min
        for i in range(3):
            for j in range(3):
                if i != j:
                    res = min(res, y_nums - y[i] + r_nums - rest[j])

        return res


s = Solution()
print(s.minimumOperationsToWriteY([[1, 2, 2], [1, 1, 0], [0, 1, 0]]))
print(s.minimumOperationsToWriteY([[0, 0, 1], [0, 0, 2], [1, 0, 2]]))
print(s.minimumOperationsToWriteY([[0, 1, 0, 1, 0], [2, 1, 0, 1, 2], [
      2, 2, 2, 0, 1], [2, 2, 2, 2, 2], [2, 1, 2, 2, 2]]))
