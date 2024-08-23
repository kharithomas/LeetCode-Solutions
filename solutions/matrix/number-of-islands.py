from collections import deque
from typing import List

# TC : O(m * n)
# SC : O(m * n)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        res = 0

        def dfs(y, x):
            stack = [(y, x)]
            count = 0

            while stack:
                row, col = stack.pop()

                if (row, col) in visited:
                    continue

                visited.add((row, col))
                count += 1

                for dy, dx in directions:
                    next_row, next_col = dy + row, dx + col

                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1
                    ):
                        stack.append((next_row, next_col))

            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    res = max(res, area)

        return res


s = Solution()

print(s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
