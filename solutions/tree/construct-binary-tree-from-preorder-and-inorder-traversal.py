from typing import List, Optional

from helpers.tree import TreeNode, print_tree

# TC : O(N)
# SC : O(N)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash Table for O(1) index look-up
        seen = {}
        for i, n in enumerate(inorder):
            seen[n] = i

        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            mid = seen[root_val]
            left_size = mid - in_left

            root.left = helper(pre_left + 1, pre_left +
                               left_size, in_left, mid - 1)
            root.right = helper(pre_left + left_size + 1,
                                pre_right, mid + 1, in_right)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


s = Solution()

root = s.buildTree(preorder=[1, 2, 4, 5, 3, 6], inorder=[4, 2, 5, 1, 3, 6])
print_tree(root)
