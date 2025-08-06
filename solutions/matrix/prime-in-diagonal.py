# TC: O(m*n)
# SC: O(1)

import math
from typing import List


class Solution:
    def isPrime(self, num: int) -> bool:
        if num <= 1:
            return False

        if num == 2:
            return True

        if num % 2 == 0:
            return False

        # Get square root rounded down
        num_sqrt = math.isqrt(num)

        for i in range(3, num_sqrt + 1, 2):
            if num % i == 0:
                return False

        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        rows = len(nums)
        res = 0

        for r in range(rows):
            # Primary diagonal
            if self.isPrime(nums[r][r]):
                res = max(res, nums[r][r])

            # Secondary diagonal
            c = rows - r - 1
            if r != c and self.isPrime(nums[r][c]):
                res = max(res, nums[r][c])

        return res


s = Solution()
print(s.diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
print(s.diagonalPrime([[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
