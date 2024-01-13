# TC: O(log n)
# SC: O(1)

from typing import List


class Solution:
    def modifiedBinarySearch(self, arr: List[int], target: int, left: int, right: int):
        # stop condition
        if left > right:
            return -1

        mid = left + (right - left) // 2  # overflow-safe version

        if arr[mid] == target:
            return mid

        # left subarray is sorted
        if arr[left] <= arr[mid]:

            # target is possibly in left subarray
            if target >= arr[left] and target <= arr[mid]:
                return self.modifiedBinarySearch(arr, target, left, mid - 1)

            # target is possibly in right subarray
            return self.modifiedBinarySearch(arr, target, mid + 1, right)

        # right subarray is sorted
        else:
            # target is possibly in right subarray
            if target >= arr[mid] and target <= arr[right]:
                return self.modifiedBinarySearch(arr, target, mid + 1, right)

            # target is possibly in left subarray
            return self.modifiedBinarySearch(arr, target, left, mid - 1)

    def search(self, nums: List[int], target: int) -> int:
        return self.modifiedBinarySearch(nums, target, 0, len(nums) - 1)


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([1], 0))
