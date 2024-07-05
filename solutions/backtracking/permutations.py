from typing import List

# TC : O(n * n!)
# SC : O(n)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, state = [], []

        def backtrack():
            if len(state) == len(nums):
                res.append(state.copy())
                return

            for i in range(len(nums)):
                # prevent duplicates
                if nums[i] in state:
                    continue

                state.append(nums[i])
                backtrack()
                state.pop()

        backtrack()
        return res


s = Solution()

print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
print(s.permute([1]))
