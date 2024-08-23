from collections import deque
from typing import List

# TC : O(m * n)
# SC : O(min(m,n))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        islands = 0

        def dfs(y, x):
            stack = [(y, x)]

            while stack:
                row, col = stack.pop()
                visited.add((row, col))

                for dy, dx in directions:
                    next_row, next_col = dy + row, dx + col

                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and (next_row, next_col) not in visited
                        and grid[next_row][next_col] == "1"
                    ):
                        stack.append((next_row, next_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands


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
