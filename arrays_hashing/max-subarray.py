# TC : O(n)
# SC : O(1)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0

        for n in nums:
            currentSum = max(n, currentSum + n)
            maxSum = max(currentSum, maxSum)

        return maxSum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
