# TC : O(N * K); N is number of words, K is avg. length of each word
# SC : O(1); extra space

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = {}

        for word in strs:
            counts = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                counts[index] += 1

            key = tuple(counts)  # linear operation so TC here is O(26)
            if visited.get(key) is None:
                visited[key] = [word]
            else:
                visited[key].append(word)

        return visited.values()


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
