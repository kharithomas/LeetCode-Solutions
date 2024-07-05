from typing import List

# TC : O(n * n!), This is an approximation. Also, extra n because time to copy state.
# SC : O(n), as the depth of the call stack is same as length of state, which is limited to n.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, state = [], []

        def backtrack():
            if len(state) == len(nums):
                res.append(state.copy())
                return

            for n in nums:
                # prevent duplicates
                if n in state:
                    continue

                state.append(n)
                backtrack()
                state.pop()

        backtrack()
        return res


s = Solution()

print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
print(s.permute([1]))
