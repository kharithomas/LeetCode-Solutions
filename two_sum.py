from typing import List

# time : O(n)
# space : O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        result = []
        for i, num in enumerate(nums):
            if comps.get(num) is None:
                comps[target - num] = i
            else:
                result = [comps[num], i]
        return result


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))
print(s.twoSum([2,5], 4))