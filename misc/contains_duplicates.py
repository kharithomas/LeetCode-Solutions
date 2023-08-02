# check if string contains duplicates ( best solution without sorting ) 

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = dict()

        for i, num in enumerate(nums):
            if arr.get(num) is None:
                arr[num] = 1
            else:
                return True

        return False


s = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))