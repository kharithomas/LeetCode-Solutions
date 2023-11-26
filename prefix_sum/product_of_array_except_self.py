# TC: O(N)
# SC: O(1); doesn't include result array


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
