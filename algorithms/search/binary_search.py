from typing import List


class Solution:
    def binarySearch(self, low: int, high: int, arr: List[int], target: int) -> bool:
        while low <= high:
            mid = low + (high - low) // 2

            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


s = Solution()
print(s.binarySearch(0, 4, [1, 2, 3, 4, 5], 2))
print(s.binarySearch(0, 4, [1, 3, 4, 5], 2))
