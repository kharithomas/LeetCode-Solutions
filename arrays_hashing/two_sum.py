from typing import List

# TC : O(N)
# SC : O(N)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            comp = target - n
            if seen.get(comp) is not None:
                return [seen[comp], i]

            seen[n] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
print(s.twoSum([2, 5], 4))
