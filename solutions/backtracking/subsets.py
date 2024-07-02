from typing import List

# TC : O(2^n)
# SC : O(n)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, state = [], []

        def backtrack(i: int):
            if i == len(nums):
                res.append(state.copy())
                return

            # don't pick nums[i]
            backtrack(i + 1)

            # pick nums[i]
            state.append(nums[i])
            backtrack(i + 1)
            state.pop()

        backtrack(0)
        return res


s = Solution()

print(s.subsets([1, 2, 3]))
print(s.subsets([0]))
