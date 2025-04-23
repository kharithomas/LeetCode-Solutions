# TC: O(n)
# SC: O(1)

from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = res = 0
        q = deque()
        min_q, max_q = deque(), deque()

        for r, num in enumerate(nums):
            # maintain min_q
            while min_q and min_q[-1] > num:
                min_q.pop()
            min_q.append(num)

            # maintain max_q
            while max_q and max_q[-1] < num:
                max_q.pop()
            max_q.append(num)

            # shrink window, if necessary
            if max_q[0] - min_q[0] > limit:
                if nums[l] == min_q[0]:
                    min_q.popleft()
                if nums[l] == max_q[0]:
                    max_q.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res


s = Solution()

print(s.longestSubarray([8, 2, 4, 7], 4))
print(s.longestSubarray([10, 1, 2, 4, 7, 2], 5))
print(s.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
