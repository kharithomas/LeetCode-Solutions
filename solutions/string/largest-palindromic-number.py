# TC : O(N)
# SC : O(1), extra space

class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = [0] * 10
        center = ""
        first_half = []

        for n in num:
            i = int(n)
            counts[i] += 1

        for n in range(9, -1, -1):
            if counts[n] > 0:
                if counts[n] == 1:
                    if center == "":
                        center = str(n)
                else:
                    if not first_half and n == 0:
                        continue

                    pairs = counts[n] // 2
                    first_half.append(str(n) * pairs)

                    if counts[n] % 2 != 0 and center == "":
                        center = str(n)

        # edge case - all zeros
        if not center and not first_half:
            return "0"

        return "".join(first_half + [center] + first_half[::-1])


s = Solution()

print(s.largestPalindromic("444947137"))
print(s.largestPalindromic("00009"))
print(s.largestPalindromic("0000"))
