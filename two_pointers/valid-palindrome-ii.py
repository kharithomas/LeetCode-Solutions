class Solution:
    def isPalindromic(self, s: str, start: int, end: int) -> bool:

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                is_left_palindromic = self.isPalindromic(s, start + 1, end)
                is_right_palindromic = self.isPalindromic(s, start, end - 1)

                return is_left_palindromic or is_right_palindromic                    

            start += 1
            end -= 1

        return True
    
s = Solution()
print(s.validPalindrome("aba"))
print(s.validPalindrome("abca"))
print(s.validPalindrome("abc"))
