# TC: O(n)
# SC: O(1)

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        curr_product = 1

        for n in nums:
            curr_product = max(curr_product * n, n)
            max_product = max(curr_product, max_product)

        return max_product


s = Solution()
print(s.maxProduct([-2, 3, -4]))
