from typing import List

# TC : O(n*2^n), where n represents value of target
# SC : O(n)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, state = [], []
        candidates.sort()

        def backtrack(start: int, remaining: int):
            if remaining == 0:
                res.append(state.copy())
            elif remaining > 0:
                for i in range(start, len(candidates)):
                    state.append(candidates[i])
                    remaining -= candidates[i]
                    backtrack(i, remaining)
                    state.pop()
                    remaining += candidates[i]

        backtrack(0, target)
        return res


s = Solution()

print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2], 1))
