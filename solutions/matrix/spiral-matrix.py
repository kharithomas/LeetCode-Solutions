# TC: O(m*n)
# SC: O(1)

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        res = []

        while left <= right and top <= bottom:
            # Move right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # Move down
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # Move left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Move up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
    
s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))