# reverse a 32 bit signed integer

class Solution:
    def checkOverflow(self, x:int) -> bool:
        if x < -2**31 or x > 2**31-1:
            return True
        return False

    def reverse(self, x:int):
        strX = str(x)
        result = 0
        if self.checkOverflow(x):
            return result
        elif strX[0] == '-':
            sub = strX[1:]
            val = int(sub[::-1]) * -1
            if self.checkOverflow(val):
                return result
            else:
                result = val
        else:
            val = int(strX[::-1])
            if self.checkOverflow(val):
                return result
            else:
                result = val
        return result


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(0))
print(s.reverse(-2**29))
print(s.reverse(153423646))

