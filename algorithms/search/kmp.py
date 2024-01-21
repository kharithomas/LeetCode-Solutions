# TC: O(n + m); n is length of text and m is length of pattern
# SC: O(m)

from typing import List


class Solution:

    def build_lps_array(self, pattern: str) -> List[str]:
        """Builds the Longest Prefix Suffix (LPS) array for a given pattern"""

        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                i += 1

        return lps

    def kmp(self, text: str, pattern: str) -> bool:
        """Efficiently searches for a substring (pattern) in a given text"""

        lps = self.build_lps_array(pattern)  # Both TC and SC are O(m)
        i, j = 0, 0

        while i < len(text) and j < len(pattern):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1

        return j == len(pattern)


s = Solution()
print(s.kmp("abcxabcdabcdabcy", "abcdabcy"))
