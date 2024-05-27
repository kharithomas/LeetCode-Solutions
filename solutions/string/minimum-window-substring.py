# TC : O(N+K), where N is length of s and K is length of t.
# SC : O(N+K)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = None

        # create the frequency dict for t
        freqT = {}
        for char in t:
            freqT[char] = 1 + freqT.get(char, 0)

        # traverse string and create our window
        window = {}
        have, need = 0, len(freqT)
        l = 0
        for r in range(len(s)):
            # add character to window
            window[s[r]] = 1 + window.get(s[r], 0)

            # check if we need this letter in this quantity
            if s[r] in freqT and window[s[r]] == freqT[s[r]]:
                have += 1

            # if our window is valid
            while have == need:
                # check if window is smallest so far
                if res is None or (r - l + 1) < len(res):
                    res = s[l: r + 1]

                # shrink window
                window[s[l]] -= 1

                # if by removing this we drop below our need
                if s[l] in freqT and window[s[l]] < freqT[s[l]]:
                    have -= 1

                l += 1

        return res if res else ""


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "a"))
print(s.minWindow("a", "aa"))
