from collections import deque
from typing import List

# TC : O(m * n)
# SC : O(m * n)


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0 and (r, c) not in visited:
                    q.append((r, c, 0))
                    visited.add((r, c))

        res = [row[:] for row in mat]
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        while q:
            r, c, steps = q.popleft()

            if mat[r][c] == 1:
                res[r][c] = steps

            for dy, dx in directions:
                next_row, next_col = dy + r, dx + c

                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and (next_row, next_col) not in visited
                ):
                    q.append((next_row, next_col, steps + 1))
                    visited.add((next_row, next_col))

        return res


s = Solution()

print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
