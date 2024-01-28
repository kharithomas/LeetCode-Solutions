# TC: O(n)
# SC: O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            curr_area = (right - left) * min(height[right], height[left])
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
