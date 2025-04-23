# TC: O(m + n + len(indices))
# SC: O(m + n)

from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_counts = [0] * m
        col_counts = [0] * n

        for r, c in indices:
            row_counts[r] += 1
            col_counts[c] += 1

        odd_rows = sum(1 for x in row_counts if x % 2 == 1)
        odd_cols = sum(1 for x in col_counts if x % 2 == 1)

        return odd_rows * n + odd_cols * m - 2 * odd_cols * odd_rows


s = Solution()

print(s.oddCells(2, 3, [[0, 1], [1, 1]]))
print(s.oddCells(2, 2, [[1, 1], [0, 0]]))
