# TC: O(m^2*n), since we repeat at most m times (each crush decreases height)
# SC: O(m*n)

from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0])
        found = True  # tracks if we have candies to crush

        while found:
            found = False
            to_crush = set()

            # Find candies to crush (horizontal)
            for r in range(rows):
                for c in range(cols-2):
                    if board[r][c] and board[r][c] == board[r][c+1] == board[r][c+2]:
                        to_crush.update({(r, c), (r, c+1), (r, c+2)})

            # Find candies to crush (vertical)
            for r in range(rows-2):
                for c in range(cols):
                    if board[r][c] and board[r][c] == board[r+1][c] == board[r+2][c]:
                        to_crush.update({(r, c), (r+1, c), (r+2, c)})

            # If we have candies to crush, crush them.
            if to_crush:
                found = True
                for r, c in to_crush:
                    board[r][c] = 0

            # Apply gravity (drop candies)
            for c in range(cols):
                write_idx = rows - 1  # Start from bottom

                for r in range(rows - 1, -1, -1):
                    if board[r][c] != 0:
                        board[write_idx][c] = board[r][c]
                        write_idx -= 1

                # Fill remaining with zeros
                for r in range(write_idx, -1, -1):
                    board[r][c] = 0

        return board


s = Solution()

print(s.candyCrush([
    [110, 5, 112, 113, 114],
    [210, 211, 5, 213, 214],
    [310, 311, 3, 313, 314],
    [410, 411, 412, 5, 414],
    [5, 1, 512, 3, 3],
    [610, 4, 1, 613, 614],
    [710, 1, 2, 713, 714],
    [810, 1, 2, 1, 1],
    [1, 1, 2, 2, 2],
    [4, 1, 4, 4, 1014]
]))
print(s.candyCrush([
    [1, 3, 5, 5, 2],
    [3, 4, 3, 3, 1],
    [3, 2, 4, 5, 2],
    [2, 4, 4, 5, 5],
    [1, 4, 4, 1, 1]
]))
