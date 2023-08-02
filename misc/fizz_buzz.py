# prints fizz buzz on ints divisible by 3 or 5 or both

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [None] * n
        for i in range(0, n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                ans[i] = 'FizzBuzz'
            elif (i+1) % 3 == 0:
                ans[i] = 'Fizz'
            elif (i+1) % 5 == 0:
                ans[i] = 'Buzz'
            else:
                ans[i] = str(i+1)

        return ans


s = Solution()
print(s.fizzBuzz(3))
print(s.fizzBuzz(5))
print(s.fizzBuzz(15))