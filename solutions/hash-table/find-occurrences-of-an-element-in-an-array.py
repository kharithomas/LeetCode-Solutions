# TC: O(N + Q), where N is length of nums and Q queries
# SC: O(N)

from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurrences = {}
        for i in range(len(nums)):
            if nums[i] in occurrences:
                occurrences[nums[i]].append(i)
            else:
                occurrences[nums[i]] = [i]

        res = []
        for q in queries:
            if x in occurrences and q <= len(occurrences[x]):
                res.append(occurrences[x][q - 1])
            else:
                res.append(-1)

        return res

s = Solution()
print(s.occurrencesOfElement([1,3,1,7], [1,3,2,4], 1))
print(s.occurrencesOfElement([1,2,3], [10], 5))