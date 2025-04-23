# TC: O(n)
# SC: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        while x >= div * 10:
            div *= 10

        while x:
            right = x % 10
            left = x // div
            if right != left:
                return False

            x = (x % div) // 10
            # we use 100 because we "chop" 2 digits off (10*10 == 100)
            div //= 100

        return True


s = Solution()

print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(1000021))
