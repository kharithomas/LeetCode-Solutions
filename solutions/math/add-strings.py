# TC: O(max(n,m)), where n is length of num1, and m num2
# SC: O(n + m)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = []
        carry = 0

        while i >= 0 or j >= 0:
            num_i = int(num1[i]) if i >= 0 else 0
            num_j = int(num2[j]) if j >= 0 else 0

            curr_sum = carry + num_i + num_j
            carry = curr_sum // 10
            remainder = curr_sum % 10
            res.append(str(remainder))

            i -= 1
            j -= 1

        if carry:
            res.append(str(carry))

        return ''.join(reversed(res))


s = Solution()

print(s.addStrings("11", "123"))
print(s.addStrings("456", "77"))
print(s.addStrings("0", "0"))
