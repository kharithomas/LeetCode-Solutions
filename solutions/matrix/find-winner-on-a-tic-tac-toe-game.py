# TC: O(1), since there's only 9 board positions
# SC: O(1)

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a, b = [0] * 8, [0] * 8

        for i in range(len(moves)):
            if i % 2 == 0:
                player = a
            else:
                player = b

            r, c = moves[i]
            player[r] += 1  # row
            player[c + 3] += 1  # col

            # primary diagonal
            if r == c:
                player[6] += 1

            # secondary diagonal
            if r == 2 - c:
                player[7] += 1

        for i in range(len(a)):
            if a[i] == 3:
                return "A"
            if b[i] == 3:
                return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"


s = Solution()
print(s.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
print(s.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
print(s.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0],
      [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))
