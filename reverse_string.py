# reverse string in place

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first, last = 0, len(s)-1
        while last > first:
            # swap
            temp = s[first]
            s[first] = s[last]
            s[last] = temp

            # s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1


s = Solution()
s.reverseString(['h','e','l','l','o'])
s.reverseString(['k','h','a','r','i'])
s.reverseString(['r','a','c','e','c','a','r'])