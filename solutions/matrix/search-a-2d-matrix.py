# TC: O(log(m*n))
# SC: O(1)

from typing import List


class Solution:
    def binarySearch(self, low: int, high: int, arr: List[int], target: int) -> bool:
        while low <= high:
            mid = low + (high - low) // 2

            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows - 1

        # Find potential row
        while low <= high:
            mid = low + (high - low) // 2

            # This middle row may contain the value - search it
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                return self.binarySearch(0, cols - 1, matrix[mid], target)

            # Search in left or right rows
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        return False


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(s.searchMatrix([[1]], 1))
