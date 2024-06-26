from typing import List


class Codec:
    # TC : O(N), where N is the length of strs
    # SC : O(K), where K denotes the extra space to store the delimeter and word length
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    # TC : O(N), where N is the length of s
    # SC : O(K), where K denotes the extra space to store the delimeter and word length
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []

        l = 0
        while l < len(s):
            r = l + 1

            while s[r] != "#":
                r += 1

            word_len = int(s[l:r])
            word_start = r + 1
            word_end = word_start + word_len
            res.append(s[word_start:word_end])

            l = word_end

        return res


codec = Codec()
print(codec.decode(codec.encode(["Hello", "World"])))
print(codec.decode(codec.encode([""])))
