# reverse bit string

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            outcome = n & 1
            n >>= 1
            result <<= 1
            result |= outcome

        return result


s = Solution()
print(s.reverseBits(0b00000010100101000001111010011100))