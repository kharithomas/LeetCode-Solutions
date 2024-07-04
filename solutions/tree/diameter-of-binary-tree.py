from typing import Optional

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        stack = []
        depths = {}
        curr, prev = root, None

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]

            if not curr.right or curr.right == prev:
                stack.pop()

                # find depth of child nodes, if exists
                left_depth = depths.get(curr.left, 0)
                right_depth = depths.get(curr.right, 0)

                # store max depth for current node
                depths[curr] = max(left_depth, right_depth) + 1

                # update max diameter, if necessary
                diameter = left_depth + right_depth
                res = max(res, diameter)

                prev = curr
                curr = None
            else:
                curr = curr.right

        return res


s = Solution()

a = TreeNode(2)
a.left = TreeNode(4)
a.right = TreeNode(5)

root = TreeNode(1)
root.left = a
root.right = TreeNode(3)

print(s.diameterOfBinaryTree(root))

root = TreeNode(1)
root.left = TreeNode(2)

print(s.diameterOfBinaryTree(root))
