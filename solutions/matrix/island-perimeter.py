# TC: O(m*n)
# SC: O(1)

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 4
                    if r > 0 and grid[r-1][c] == 1:
                        res -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        res -= 2

        return res


s = Solution()
print(s.islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(s.islandPerimeter([[1]]))
print(s.islandPerimeter([[1, 0]]))
