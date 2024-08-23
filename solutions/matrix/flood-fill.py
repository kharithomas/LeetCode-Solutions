from collections import deque
from typing import List

# TC : O(m * n)
# SC : O(m * n)


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        res = [row[:] for row in image]

        def bfs(y, x, starting_pixel):
            q = deque([(y, x)])
            while q:
                row, col = q.popleft()

                if (row, col) in visited:
                    continue

                visited.add((row, col))
                res[row][col] = color

                for dy, dx in directions:
                    next_row, next_col = dy + row, dx + col

                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and image[next_row][next_col] == starting_pixel
                    ):
                        q.append((next_row, next_col))

        bfs(sr, sc, res[sr][sc])
        return res


s = Solution()

print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
