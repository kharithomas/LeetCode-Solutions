from typing import Optional

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(t1, t2):
            if not t1 and not t2:
                return True

            if not t1 or not t2:
                return False

            if t1.value != t2.value:
                return False

            return helper(t1.left, t2.right) and helper(t1.right, t2.left)

        if not root:
            return True

        return helper(root.left, root.right)


s = Solution()

p = TreeNode(2)
p.left = TreeNode(4)
p.right = TreeNode(3)

q = TreeNode(2)
q.left = TreeNode(3)
q.right = TreeNode(4)

root = TreeNode(1)
root.left = q
root.right = p

print(s.isSymmetric(root))

a = TreeNode(2)
a.left = TreeNode(3)

root = TreeNode(1)
root.left = a
root.right = a

print(s.isSymmetric(root))
