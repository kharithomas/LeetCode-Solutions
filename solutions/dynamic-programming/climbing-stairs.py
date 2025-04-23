# TC: O(N)
# SC: O(N)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)

        for i in range(n+1):
            if i < 2:
                memo[i] = 1
            else:
                memo[i] = memo[i-1] + memo[i-2]

        return memo[n]


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(44))
