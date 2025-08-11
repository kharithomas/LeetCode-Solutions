# TC: O(m*n)
# SC: O(1), extra-space

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        counter = 1
        res = [[0] * n for _ in range(n)]
        left, right = 0, len(res[0]) - 1
        top, bottom = 0, len(res) - 1

        while left <= right and top <= bottom:
            # Move right
            for col in range(left, right + 1):
                res[top][col] = counter
                counter += 1
            top += 1

            # Move down
            for row in range(top, bottom + 1):
                res[row][right] = counter
                counter += 1
            right -= 1

            # Move left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res[bottom][col] = counter
                    counter += 1
                bottom -= 1

            # Move up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[row][left] = counter
                    counter += 1
                left += 1

        return res


s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(1))
