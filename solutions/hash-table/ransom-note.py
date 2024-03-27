# TC : O(n), where n is length of ransom note
# TC : O(26), since there 26 lowercase English letters

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqM = {}

        for c in magazine:
            freqM[c] = 1 + freqM.get(c, 0)

        for c in ransomNote:
            if freqM.get(c) is None or freqM[c] == 0:
                return False

            freqM[c] -= 1

        return True


s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
