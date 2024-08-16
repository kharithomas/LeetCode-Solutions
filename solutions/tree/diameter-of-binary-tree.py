from typing import Optional

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def helper(node: Optional[TreeNode]):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            nonlocal res
            res = max(res, left + right)

            return 1 + max(left, right)

        helper(root)
        return res


s = Solution()

a = TreeNode(2)
a.left = TreeNode(4)
a.right = TreeNode(5)

root = TreeNode(1)
root.left = a
root.right = TreeNode(3)

print(s.diameterOfBinaryTree(root))

root = TreeNode(1)
root.left = TreeNode(2)

print(s.diameterOfBinaryTree(root))
