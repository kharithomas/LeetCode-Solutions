# find missing number

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        realSum = len(nums)
        sum = 0
        for i in range(len(nums)):
            realSum += i
            sum += nums[i]

        return realSum - sum


s = Solution()
print(s.missingNumber([3, 0, 1]))
print(s.missingNumber([0, 1]))
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
