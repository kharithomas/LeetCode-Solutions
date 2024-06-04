from typing import Optional

from helpers.tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


s = Solution()

b = TreeNode(9)

c = TreeNode(20)
c.left = TreeNode(15)
c.right = TreeNode(7)

a = TreeNode(3)
a.left = b
a.right = c

print(s.maxDepth(a))
