from typing import List

# TC : O(m * n), where m is number of rows, n is number of cols
# SC : O(m * n), because call-stack can have at most m*n calls


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        # Marks all connected land masses visited
        def traverse(row, col):
            if grid[row][col] == "0":
                return

            # Mark as visited
            grid[row][col] = "0"

            for y_offset, x_offset in directions:
                new_row = y_offset + row
                new_col = x_offset + col

                # Check pos within grid boundary
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    traverse(new_row, new_col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    traverse(row, col)

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
