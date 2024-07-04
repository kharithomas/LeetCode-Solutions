from typing import List

# TC : O(2^n)
# SC : O(n)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, state = [], []
        nums.sort()

        def backtrack(start: int):
            res.append(state.copy())

            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue

                state.append(nums[i])
                backtrack(i + 1)
                state.pop()

        backtrack(0)
        return res


s = Solution()

print(s.subsetsWithDup([1, 2, 2]))
print(s.subsetsWithDup([0]))
