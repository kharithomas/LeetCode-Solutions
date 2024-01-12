# TC: O(n)
# SC: O(1)

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        curr_max, curr_min = 1, 1

        for n in nums:
            temp = curr_max * n
            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(temp, curr_min * n, n)
            max_product = max(curr_max, max_product)

        return max_product


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2, 0, -1]))
