from typing import Optional

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.isBalanced(root.left)
        if not left:
            return False

        right = self.isBalanced(root.right)
        if not right:
            return False

        if abs(left - right) > 1:
            return False

        return 1 + max(left, right)


s = Solution()

a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(7)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = a

print(s.isBalanced(root))

a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(7)

b = TreeNode(20)
b.left = a
b.right = TreeNode(7)

root = TreeNode(3)
root.left = b
root.right = TreeNode(9)

print(s.isBalanced(root))
