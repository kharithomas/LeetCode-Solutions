# TC: O(m*n)
# SC: O(m*n)

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        if (r * c) != (rows * cols):
            return mat

        curr_row = 0
        res = [[] for _ in range(r)]
        for y in range(rows):
            for x in range(cols):
                if (len(res[curr_row]) == c):
                    curr_row += 1
                res[curr_row].append(mat[y][x])

        return res


s = Solution()

m1 = [[1, 2], [3, 4]]
print("Before:", m1)
print("After:", s.matrixReshape(m1, 1, 4))

m2 = [[1, 2], [3, 4]]
print("Before:", m2)
print("After:", s.matrixReshape(m2, 2, 4))
