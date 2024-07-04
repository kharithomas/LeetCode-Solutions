from typing import Optional

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode]):
            if not node:
                return True

            left = helper(node.left)
            right = helper(node.right)

            # both children are not univalue
            if not left or not right:
                return False

            # left child exists but doesn't match
            if node.left and node.value != node.left.value:
                return False

            # right child exists but doesn't match
            if node.right and node.value != node.right.value:
                return False

            self.res += 1
            return True

        self.res = 0
        helper(root)
        return self.res


s = Solution()

a = TreeNode(1)
a.left = TreeNode(5)
a.right = TreeNode(5)

b = TreeNode(1)
b.right = TreeNode(5)

root = TreeNode(1)
root.left = a
root.right = b

print(s.countUnivalSubtrees(root))
