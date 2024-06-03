# TC : O(log n)
# SC : O(1)

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        low, high = 0, len(nums) - 1
        while low <= high:
            # array is not rotated
            if nums[low] <= nums[high]:
                return min(res, nums[low])

            mid = low + (high - low) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
