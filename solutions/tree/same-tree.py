from typing import Optional

from helpers.tree import TreeNode

# TC : O(p + q), where p and q represent the number of nodes in each tree, respectively.
# SC : O(p + q)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both treeNodes are null
        if not p and not q:
            return True

        # only one treeNode is null
        if not p or not q:
            return False

        # values don't match
        if p.value != q.value:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right


s = Solution()

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(s.isSameTree(p, q))

m = TreeNode(1)
m.left = TreeNode(2)

n = TreeNode(1)
n.right = TreeNode(2)

print(s.isSameTree(m, n))
