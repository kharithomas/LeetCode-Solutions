# TC: O(m*n)
# SC: O(1)

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        y, x = 0, 0
        up = True
        res = []

        while len(res) < rows * cols:
            res.append(mat[y][x])

            if up:
                if x == cols - 1:  # If at last column, move down
                    y += 1
                    up = False
                elif y == 0:  # If at first row, move right
                    x += 1
                    up = False
                else:  # Otherwise, move diagonally up-right
                    y -= 1
                    x += 1
            else:
                if y == rows - 1:  # If at last row, move right
                    x += 1
                    up = True
                elif x == 0:  # If at first column, move down
                    y += 1
                    up = True
                else:  # Otherwise, move diagonally down-left
                    y += 1
                    x -= 1
        
        return res
    
s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.findDiagonalOrder([[1,2],[3,4]]))