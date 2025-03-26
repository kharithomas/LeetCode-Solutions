# TC: O(N), where N is len of queries
# SC: O(N), where N is len of queries

from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_freq = {}
        ball_colors = {}
        res = []

        for ball, color in queries:
            if ball in ball_colors:
                # get old color
                old_color = ball_colors[ball] 
                
                # decrease old color freq.
                color_freq[old_color] -= 1

                # remove key if necessary
                if color_freq[old_color] == 0:
                    color_freq.pop(old_color)
            
            # add or increase
            color_freq[color] = color_freq.get(color, 0) + 1

            # assign new color
            ball_colors[ball] = color

            # take result
            res.append(len(color_freq))

        return res


s = Solution()
print(s.queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))
print(s.queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]))
