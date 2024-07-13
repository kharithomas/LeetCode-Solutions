from typing import Optional

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = helper(root.left)
            if left == -1:
                return -1

            right = helper(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return helper(root) != -1


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
