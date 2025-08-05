# TC : O(m*n)
# SC : O(1)

from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)

        for r in range(rows):
            for c in range(len(words[r])):
                # Check if the transposed position exists
                if c >= rows or r >= len(words[c]):
                    return False
                if words[r][c] != words[c][r]:
                    return False

        return True


s = Solution()
print(s.validWordSquare(["abcd", "bnrt", "crmy", "dtye"]))
print(s.validWordSquare(["abcd", "bnrt", "crm", "dt"]))
print(s.validWordSquare(["ball", "area", "read", "lady"]))
