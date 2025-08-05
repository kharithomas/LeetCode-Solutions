# TC : O(n^2), where n is both row and col size
# SC : O(1)

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = cols = len(image)

        # 1. horizontal flip cols
        start, end = 0, cols - 1
        while start < end:
            for r in range(rows):
                image[r][start], image[r][end] = image[r][end], image[r][start]
            start += 1
            end -= 1

        # 2. invert values
        for c in range(cols):
            for r in range(rows):
                image[r][c] = 0 if image[r][c] == 1 else 1

        return image


s = Solution()
print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(s.flipAndInvertImage(
    [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
