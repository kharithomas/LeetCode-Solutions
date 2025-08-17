# TC: O(m*n)
# SC: O(1)

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                # Skip first position
                if r == 0 and c == 0:
                    continue

                # If in first row, default to left
                if r == 0:
                    grid[r][c] += grid[r][c - 1]

                # If in first col, default to up
                elif c == 0:
                    grid[r][c] += grid[r - 1][c]

                # Take min of left and up
                else:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        # Last position has min sum
        return grid[rows - 1][cols - 1]


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))
