# TC: O(m*n)
# SC: O(m*n)

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # return list(zip(*matrix))
        
        rows, cols = len(matrix), len(matrix[0])
        res = [[0] * rows for _ in range(cols)]

        for y in range(rows):
            for x in range(cols):
                res[x][y] = matrix[y][x]

        return res
        

s = Solution()

m1 = [[1,2,3],[4,5,6],[7,8,9]]
print("Before:", m1)
print("After:", s.transpose(m1))

m2 = [[1,2,3],[4,5,6]]
print("Before:", m2)
print("After:", s.transpose(m2))