# TC : O(logN)
# SC : O(1)

class Solution:
    def sumOfDigits(self, n: int) -> int:
        sum = 0
        
        while n > 0:
            digit = n % 10
            n = n // 10
            sum += digit ** 2
        
        return sum
    
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfDigits(n)

        while slow != fast:
            slow = self.sumOfDigits(slow)
            fast = self.sumOfDigits(self.sumOfDigits(fast))

        return fast == 1
    
s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))