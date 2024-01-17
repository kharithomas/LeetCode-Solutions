# TC: O(n)
# SC: O(k)

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        l = r = 0

        while r < len(nums):
            # remove all smaller values than current
            while d and nums[d[-1]] < nums[r]:
                d.pop()

            # add current value to deque
            d.append(r)

            # if front of deque is outside window, remove it
            if d[0] < l:
                d.popleft()

            # if window size is k, add front of deque to result
            if r >= (k - 1):
                res.append(nums[d[0]])
                l += 1

            r += 1

        return res


s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(s.maxSlidingWindow([1], 1))
print(s.maxSlidingWindow([1, -1], 1))
