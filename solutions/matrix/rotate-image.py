# TC: O(n^2)
# SC: O(1)

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                # save top left value
                top_left = matrix[top][l + i]

                # move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = top_left
            
            l += 1
            r -= 1

s = Solution()

m1 = [[1,2,3],[4,5,6],[7,8,9]]
print(f"Before: {m1}")
s.rotate(m1)
print(f"After: {m1}")

m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(f"Before: {m2}")
s.rotate(m2)
print(f"After: {m2}")