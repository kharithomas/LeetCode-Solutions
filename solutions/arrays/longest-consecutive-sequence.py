# TC : O(N)
# SC : O(N)

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            # check if n is start of sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                res = max(res, length)

        return res


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
