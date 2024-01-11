# TC : O(n)
# SC : O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].lower().isalnum():
                start += 1
                continue

            if not s[end].lower().isalnum():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
