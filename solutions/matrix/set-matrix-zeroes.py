# TC: O(m*n)
# SC: O(1)

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        first_col_zero = False

        # Use first_col/row as markers
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_zero = True
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        # Use markers to set zeroes
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        # Handle first row and col
        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0
        
        # Handle first row and col
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0


s = Solution()

m1 = [[1,1,1],[1,0,1],[1,1,1]]
print(f'Before: ', m1)
s.setZeroes(m1)
print(f'After: ', m1)

m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(f'\nBefore: ', m2)
s.setZeroes(m2)
print(f'After: ', m2)