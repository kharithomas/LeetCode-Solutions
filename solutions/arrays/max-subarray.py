# TC: O(n)
# SC: O(1)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            curr_sum = max(n, curr_sum + n)
            max_sum = max(curr_sum, max_sum)

        return max_sum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
