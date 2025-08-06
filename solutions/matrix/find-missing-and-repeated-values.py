# TC: O(n^2)
# SC: O(n^2)

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        counts = [0] * (len(grid) ** 2)
        res = [0] * 2

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                i = grid[r][c] - 1
                counts[i] += 1

        for i in range(len(counts)):
            if counts[i] == 2:
                res[0] = i + 1
            if counts[i] == 0:
                res[1] = i + 1

        return res


s = Solution()
print(s.findMissingAndRepeatedValues([[1, 3], [2, 2]]))
print(s.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
