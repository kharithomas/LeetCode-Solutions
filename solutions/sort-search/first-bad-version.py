# TC: O(log(n))
# SC: O(1)

class Solution:
    def __init__(self, bad_version: int):
        self.bad_version = bad_version

    def isBadVersion(self, version: int) -> bool:
        return version >= self.bad_version

    # Note: everything above this line is provided by problem
    def firstBadVersion(self, n: int) -> int:
        l, h = 1, n
        while l <= h:
            m = l + (h - l) // 2
            if self.isBadVersion(m):
                if not self.isBadVersion(m - 1):
                    return m
                else:
                    h = m - 1
            else:
                l = m + 1


s = Solution(4)
print(s.firstBadVersion(5))

s.bad_version = 1
print(s.firstBadVersion(1))
