
from typing import Optional

from helpers.tree import TreeNode

# TC : O(N * M)
# SC : O(N + M)


class Solution:
    def isSameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        if t1.value != t2.value:
            return False

        left = self.isSameTree(t1.left, t2.left)
        right = self.isSameTree(t1.right, t2.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # corner case - subroot is empty
        if not subRoot:
            return True

        # corner case - root is empty
        if not root:
            return False

        # check root
        if self.isSameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right


s = Solution()

c = TreeNode(2)

a = TreeNode(4)
a.left = TreeNode(1)
a.right = c

b = TreeNode(5)

root = TreeNode(3)
root.left = a
root.right = b

sub_root = TreeNode(4)
sub_root.left = TreeNode(1)
sub_root.right = TreeNode(2)

print(s.isSubtree(root, sub_root))

c.right = TreeNode(0)

print(s.isSubtree(root, sub_root))
