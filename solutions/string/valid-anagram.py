# TC: O(n)
# SC: O(1)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case check
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for c in s:
            pos = ord(c) - ord("a")
            counts[pos] += 1

        for c in t:
            pos = ord(c) - ord("a")
            if counts[pos] == 0:
                return False

            counts[pos] -= 1

        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "ab"))
