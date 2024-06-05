from typing import Optional

from helpers.tree import TreeNode, print_tree

# TC : O(N)
# SC : O(h)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            # flip subtree
            root.right, root.left = root.left, root.right

            # recurse on left subtree
            root.left = self.invertTree(root.left)

            # recurse on right subtree
            root.right = self.invertTree(root.right)

        return root


s = Solution()

b = TreeNode(2)
b.left = TreeNode(1)
b.right = TreeNode(3)

c = TreeNode(7)
c.left = TreeNode(6)
c.right = TreeNode(9)

a = TreeNode(4)
a.left = b
a.right = c

print("Before Flip: ", end="")
print_tree(a)
print("")

s.invertTree(a)

print("After Flip: ", end=" ")
print_tree(a)
