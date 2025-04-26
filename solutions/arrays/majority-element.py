# TC: O(N)
# SC: O(1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1

        return candidate


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
