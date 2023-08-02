# find the maximum subarray - using Kadane's Algorithm

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(currSum, maxSum)

        return maxSum


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([-2,2,5,-11,6]))
print(s.maxSubArray([3, -3, 15, -4, 7, 5]))