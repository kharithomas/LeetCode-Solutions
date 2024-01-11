# TC: O(n)
# SC: O(1)

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            sum = numbers[start] + numbers[end]

            if sum == target:
                return [start + 1, end + 1]
            elif sum > target:
                end -= 1
            else:
                start += 1


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))
