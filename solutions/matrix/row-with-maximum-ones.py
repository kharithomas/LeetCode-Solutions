# TC : O(m*n), where m is the number of rows
# SC: O(1)

from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = [0, 0]

        for r in range(rows):
            count = sum(mat[r])
            if count > res[1]:
                res[0], res[1] = r, count

        return res


s = Solution()
print(s.rowAndMaximumOnes([[0, 1], [1, 0]]))
print(s.rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]))
print(s.rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]))
