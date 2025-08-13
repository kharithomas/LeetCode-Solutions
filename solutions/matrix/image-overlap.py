# TC: O(n^4), where n is # of rows
# SC: O(n^2)

from typing import List


class Solution:
    def findOnesPositions(self, matrix: List[List[int]]) -> set:
        res = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 1:
                    res.add((r, c))
        return res

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # Find position of ones for both images
        img1_ones = self.findOnesPositions(img1)
        img2_ones = self.findOnesPositions(img2)

        # For each position in img1, compare w/ distance in img2
        shift_distances = {}
        for pos1 in img1_ones:
            for pos2 in img2_ones:
                # Compute distance and update frequency
                distance = (pos2[0] - pos1[0], pos2[1] - pos1[1])
                shift_distances[distance] = 1 + \
                    shift_distances.get(distance, 0)

        # Edge case: img1_ones or img2_ones is empty
        if not shift_distances:
            return 0

        # Most freq. shift represents most overlapping 1's
        return max(shift_distances.values())


s = Solution()
print(s.largestOverlap([[1, 1, 0], [0, 1, 0], [
      0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]))
print(s.largestOverlap([[1]], [[1]]))
print(s.largestOverlap([[0]], [[0]]))
