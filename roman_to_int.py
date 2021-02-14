# convert roman numerals to int

class Solution:
    def romanToInt(self, s: str) -> int:
        alphabet = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        result = 0

        for i in range(len(s)):
            if i+1 != len(s) and alphabet[s[i]] < alphabet[s[i+1]]:
                result -= alphabet[s[i]]
            else:
                result += alphabet[s[i]]

        return result


sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("IX"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))