# TC: O(n)
# SC: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [-1] * 256
        max_length = 0
        left, right = 0, 0

        while right < len(s):
            index = ord(s[right])

            if seen[index] > -1:
                left = max(left, seen[index] + 1)

            max_length = max(right - left + 1, max_length)
            seen[index] = right
            right += 1

        return max_length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
