from typing import Optional

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            # since there is no further down we can go,
            # just check if our path equals target
            return targetSum == 0

        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)

        return left or right


s = Solution()

a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(7)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = a

print(s.hasPathSum(root))

a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(7)

b = TreeNode(20)
b.left = a
b.right = TreeNode(7)

root = TreeNode(3)
root.left = b
root.right = TreeNode(9)

print(s.hasPathSum(root))
