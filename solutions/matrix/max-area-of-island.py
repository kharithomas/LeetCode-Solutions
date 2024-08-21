from collections import deque
from typing import List

# TC : O(m * n), where m is number of rows, n is number of cols
# SC : O(min(m,n))


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def bfs(row: int, col: int) -> int:
            q = deque([(row, col)])
            area = 0

            while q:
                r, c = q.popleft()

                if grid[r][c] == 0:
                    continue

                area += 1
                grid[r][c] = 0

                for y_offset, x_offset in directions:
                    new_row = r + y_offset
                    new_col = c + x_offset

                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        q.append((new_row, new_col))

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    res = max(res, area)

        return res


s = Solution()

print(s.maxAreaOfIsland([
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

print(s.maxAreaOfIsland([
    [0, 0, 0, 0, 0, 0, 0, 0]
]))
