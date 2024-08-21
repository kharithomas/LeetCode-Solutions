from collections import deque
from typing import List

# TC : O(m * n), where m is number of rows, n is number of cols
# SC : O(min(m,n))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        # Marks all connected land masses visited
        def bfs(row: int, col: int):
            q = deque([(row, col)])

            while q:
                r, c = q.popleft()

                if grid[r][c] == "0":
                    continue

                # Mark as visited
                grid[r][c] = "0"

                for y_offset, x_offset in directions:
                    new_row = y_offset + r
                    new_col = x_offset + c

                    # Check pos within grid boundary
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        q.append((new_row, new_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)

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
