# TC: O(max(m, n))
# SC: O(max(m, n))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        a_ptr, b_ptr = len(a) - 1, len(b) - 1

        while a_ptr >= 0 or b_ptr >= 0:
            total = carry

            if a_ptr >= 0:
                total += int(a[a_ptr])

            if b_ptr >= 0:
                total += int(b[b_ptr])

            carry = total // 2
            result = total % 2
            res.append(str(result))
            a_ptr -= 1
            b_ptr -= 1

        if carry:
            res.append(str(carry))

        return ''.join(reversed(res))


s = Solution()
print(s.addBinary("11", "1"))
print(s.addBinary("1010", "1011"))
