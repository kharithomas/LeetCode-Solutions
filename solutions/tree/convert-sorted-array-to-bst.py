from typing import List, Optional

from helpers.tree import TreeNode, print_tree

# TC : O(N)
# SC : O(logN), since the tree is height balanced.


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recurse(low: int, high: int):
            if low > high:
                return None

            mid = low + (high - low) // 2
            root = TreeNode(nums[mid])

            root.left = recurse(low, mid - 1)
            root.right = recurse(mid + 1, high)

            return root

        return recurse(0, len(nums) - 1)


s = Solution()

print_tree(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
print()
print_tree(s.sortedArrayToBST([1, 3]))
