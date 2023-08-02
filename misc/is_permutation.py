# check if two strings are permutation of one another

class Solution:
    def produceMap(self, word: str):
        wordMap = dict()
        strList = sorted(word)
        for i in range(len(strList)):
            wordMap[strList[i]] = 0

        return wordMap
    
    def isPermutation(self, str1: str, str2: str) -> bool:
        wordMap = self.produceMap(str1)

        if str1 is None or str2 is None:
            return False

        if len(str1) != len(str2):
            return False

        for i in range(len(str2)):
            if str2[i] not in wordMap or wordMap[str2[i]] == 1:
                return False

            wordMap[str2[i]] = 1

        return True


s = Solution()
print(s.isPermutation("abc", "cba"))
print(s.isPermutation("abc", "a"))
print(s.isPermutation("abc", "bbb"))
print(s.isPermutation("abc", "abc"))
