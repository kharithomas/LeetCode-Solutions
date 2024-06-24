from typing import Optional, List

from helpers.tree import TreeNode

# TC : O(N)
# TC : O(N)


class Solution:
    def _is_leaf(self, root: Optional[TreeNode]):
        return root and not root.left and not root.right

    def _add_left_boundary(self, root: Optional[TreeNode], res: List[int]):
        while root:
            if not self._is_leaf(root):
                res.append(root.value)

            root = root.left or root.right

    def _add_leaves(self, root: Optional[TreeNode], res: List[int]):
        if root:
            if self._is_leaf(root):
                res.append(root.value)
            else:
                self._add_leaves(root.left, res)
                self._add_leaves(root.right, res)

    def _add_right_boundary(self, root: Optional[TreeNode], res: List[int]):
        stack = []
        while root:
            if not self._is_leaf(root):
                stack.append(root.value)

            root = root.right or root.left

        res += stack[::-1]

    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        boundary = []

        if not self._is_leaf(root):
            boundary.append(root.value)

        self._add_left_boundary(root.left, boundary)
        self._add_leaves(root, boundary)
        self._add_right_boundary(root.right, boundary)

        return boundary


s = Solution()


a = TreeNode(2)
a.left = TreeNode(3)
a.right = TreeNode(4)

root = TreeNode(1)
root.right = a

print(s.boundaryOfBinaryTree(root))
