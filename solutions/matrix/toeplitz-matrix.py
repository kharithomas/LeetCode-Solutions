# TC : O(m*n)
# SC : O(1)

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                if matrix[r-1][c-1] != matrix[r][c]:
                    return False

        return True


s = Solution()
print(s.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(s.isToeplitzMatrix([[1, 2], [2, 2]]))
