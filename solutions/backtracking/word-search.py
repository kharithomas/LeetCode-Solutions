from typing import List

# TC : O((m*n)^2)
# SC : O(w), where w is length of word


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # up, right, down, left
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

        # edge case - board has one char
        if rows == 1 and cols == 1:
            return board[0][0] == word

        def backtrack(row: int, col: int, i: int) -> bool:
            # current path matches word
            if i == len(word):
                return True

            # current path doesn't match word
            if board[row][col] != word[i]:
                return False

            # Mark current pos. visited
            temp = board[row][col]
            board[row][col] = "$"

            for x_offset, y_offset in directions:
                new_row = row + y_offset
                new_col = col + x_offset

                # check new position is within board boundaries
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                    if backtrack(new_row, new_col, i + 1):
                        return True

            board[row][col] = temp

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False


s = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

print(s.exist(board, "ABCCED"))
print(s.exist(board, "SEE"))
print(s.exist(board, "ABCB"))
print(s.exist([["A"]], "A"))
