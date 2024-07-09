from typing import List

# TC : O(n*2^n), where n represents value of target
# SC : O(n)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, state = [], []
        candidates.sort()

        def backtrack(start: int, remaining: int):
            if remaining == 0:
                res.append(state.copy())
            elif remaining > 0:
                for i in range(start, len(candidates)):
                    # skip duplicates
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue

                    state.append(candidates[i])
                    remaining -= candidates[i]
                    backtrack(i + 1, remaining)
                    state.pop()
                    remaining += candidates[i]

        backtrack(0, target)
        return res


s = Solution()

print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(s.combinationSum2([2, 5, 2, 1, 2], 5))
