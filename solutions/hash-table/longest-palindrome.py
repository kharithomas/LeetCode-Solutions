# TC: O(n)
# SC: O(1), as only 52 possible chars

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_s = Counter(s)
        center = False
        res = 0

        for l in freq_s:
            remain = freq_s[l] % 2
            pairs = freq_s[l] // 2
            res += pairs * 2

            if remain and not center:
                center = True

        if center:
            res += 1

        return res


s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("aaa"))
