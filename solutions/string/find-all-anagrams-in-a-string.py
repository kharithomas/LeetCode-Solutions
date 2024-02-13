# TC: O(n)
# SC: O(1)

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        sCount, pCount = {}, {}  # fixed size since alphabet is only 26 chars

        # edge case check
        if len(s) < len(p):
            return res

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        if sCount == pCount:
            res.append(0)

        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1
            if sCount == pCount:
                res.append(l)

        return res


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
