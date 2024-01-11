# TC : O(N)
# SC : O(N), best case for python since strings are immutable

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        left = 0
        str_len = len(s)

        while left < str_len:
            while left < str_len and s[left] == " ":
                left += 1

            if left >= str_len:
                break

            right = left + 1
            while right < str_len and s[right] != " ":
                right += 1

            word = s[left:right]
            res = word if not res else f"{word} {res}"
            left = right + 1

        return res


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))
