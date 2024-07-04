from typing import List

# TC : O(2^n)
# SC : O(n)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, state = [], []

        def backtrack(start: int):
            # Base case
            res.append(state.copy())

            for i in range(start, len(nums)):
                #  Choose the current element
                state.append(nums[i])

                # Explore further with the current element
                backtrack(i + 1)

                # Backtrack: remove the current element to explore other subsets
                state.pop()

        backtrack(0)
        return res


s = Solution()

print(s.subsets([1, 2, 3]))
print(s.subsets([0]))
