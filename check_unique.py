# check if string has unique chars

class Solution:
    def checkUnique(self, name: str) -> bool:
        values = [False] * 128
        # edge case check
        if not s or len(s) > 128:
            return False

        for char in s:
            if values[ord(char)]:
                return False
            values[ord(char)] = True

        return True
        
        # word = sorted(name)
        # prev = ''
        # for char in word:
        #     if char == prev:
        #         return False
        #     prev = char
        # return True


s = Solution()
print(s.checkUnique('khari'))
print(s.checkUnique('kiara'))
print(s.checkUnique('MOM'))
print(s.checkUnique('chey'))