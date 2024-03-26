# TC: O(N^2)
# SC: O(1); extra space

class Solution:
    def _expand_around_center(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            odd = self._expand_around_center(s, i, i)
            even = self._expand_around_center(s, i, i + 1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even

        return res


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("a"))
