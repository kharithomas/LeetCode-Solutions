# TC : O(n+m)
# SC : O(1)

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        currRowNegativeIndex = cols - 1
        res = 0

        for row in grid:
            # We have not exceeded bottom left boundary and val is negative
            while currRowNegativeIndex >= 0 and row[currRowNegativeIndex] < 0:
                currRowNegativeIndex -= 1

            # currRowNegativeIndex is pointing to last positive element
            res += (cols - (currRowNegativeIndex + 1))

        return res


s = Solution()
print(s.countNegatives(
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(s.countNegatives([[3, 2], [1, 0]]))
