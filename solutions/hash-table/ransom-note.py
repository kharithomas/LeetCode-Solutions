# TC : O(N + M)
# SC : O(1), since there 26 lowercase English letters

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_m = {}
        for c in magazine:
            freq_m[c] = freq_m.get(c, 0) + 1

        for c in ransomNote:
            if freq_m.get(c) is None or freq_m[c] == 0:
                return False

            freq_m[c] -= 1

        return True


s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
