# TC: O(m*n)
# SC: O(1), extra-space

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = []
        r, c = 0, 0
        direction = 1  # up

        while r < rows and c < cols:
            # add current val to result
            res.append(mat[r][c])

            # if we're in the (first col and not last row and going down) or (last col and going up), go down row (incr. row)
            if (c == 0 and direction < 0 and r < rows - 1) or (c == cols - 1 and direction > 0):
                r += 1
                direction *= -1
            # elif we're in the (first row and going up) or (last row and going down), go right (incr. col)
            elif (r == 0 and direction > 0) or (r == rows - 1 and direction < 0):
                c += 1
                direction *= -1
            # else, go diagonally based on direction
            else:
                # if dir is up, move add col, sub row
                if direction > 0:
                    c += 1
                    r -= 1
                # else dir is down, sub col, add row
                else:
                    c -= 1
                    r += 1

        return res


s = Solution()
print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.findDiagonalOrder([[1, 2], [3, 4]]))
