from typing import List

# TC : O(N)
# SC : O(1)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = i = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1


s = Solution()

arr1 = [2, 0, 2, 1, 1, 0]
s.sortColors(arr1)
print(arr1)

arr2 = [2, 0, 1]
s.sortColors(arr2)
print(arr2)
