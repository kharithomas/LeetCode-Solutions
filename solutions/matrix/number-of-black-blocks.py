# TC: O(k), where k is len of coordinates
# SC: O(k)

from collections import defaultdict
from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        block_counts = defaultdict(int)

        for x, y in coordinates:
            cells = ((0, 0), (0, -1), (-1, 0), (-1, -1))
            for dx, dy in cells:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m - 1 and 0 <= ny < n - 1:
                    block_counts[(nx, ny)] += 1

        res = [0] * 5
        total_blocks = (m - 1) * (n - 1)

        for count in block_counts.values():
            res[count] += 1

        res[0] = total_blocks - sum(res[1:])

        return res


s = Solution()

print(s.countBlackBlocks(3, 3, [[0, 0]]))
print(s.countBlackBlocks(3, 3, [[0, 0], [1, 1], [0, 2]]))
