# TC : O(N), where N is the length of nums; Note: K will never be greater than N.
# SC : O(N), as each sublist can contain at most N elements

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1

        counts = [[] for _ in range(len(nums) + 1)]
        for key, val in freqs.items():
            counts[val].append(key)

        i = len(nums)
        while len(res) < k and i >= 0:
            while len(res) < k and len(counts[i]) > 0:
                res.append(counts[i].pop())

            i -= 1

        return res


s = Solution()

print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))
